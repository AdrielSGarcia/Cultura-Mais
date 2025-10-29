const { createApp, defineAsyncComponent } = Vue;

const app = createApp({
    data() {
        return {
            loading: true,
            currentPage: 'home',
            selectedId: null,
            mobileMenuOpen: false,
            user: null,
            homeData: {},
            noticias: {},
            artigos: {},
            editais: {},
            searchResults: {},
            alert: { show: false, type: 'info', message: '' },
            searchQuery: '',
            lastSearchQuery: ''
        };
    },

    computed: {
        activeComponent() {
            switch (this.currentPage) {
                case 'home': return 'home-component';
                case 'noticias': return 'noticias-component';
                case 'artigos': return 'artigos-component';
                case 'editais': return 'editais-component';
                case 'noticia-detail': return 'noticia-detail-component';
                case 'artigo-detail': return 'artigo-detail-component';
                case 'edital-detail': return 'edital-detail-component';
                case 'login': return 'login-component';
                case 'register': return 'register-component';
                case 'profile': return 'profile-component';
                case 'search': return 'search-results-component';
                default: return 'home-component'; // Um fallback seguro
            }
        }
    },

    async mounted() {
        await this.initializeApp();
    },
    
    methods: {
        async initializeApp() {
            try {
                const token = localStorage.getItem('access_token');
                if (token) {
                    try {
                        this.user = await apiService.getProfile();
                    } catch (error) {
                        localStorage.removeItem('access_token');
                        localStorage.removeItem('refresh_token');
                    }
                }
                this.handleRouting();
            } catch (error) {
                console.error('Erro ao inicializar a aplicação:', error);
                this.showAlert('danger', 'Erro ao carregar a aplicação.');
                this.loading = false;
            }
        },
        
        handleRouting() {
            const hash = window.location.hash.substring(1);
            const [page, id] = hash.split('/');
            this.navigateTo(page || 'home', id);
        },
        
        async navigateTo(page, id = null) {
            this.loading = true;
            this.selectedId = id;
            this.currentPage = page;
            this.mobileMenuOpen = false;
            
            window.location.hash = id ? `${page}/${id}` : page;
            
            try {
                switch (page) {
                    case 'home':
                        this.homeData = await apiService.getHomeData();
                        break;
                    case 'noticias':
                        this.noticias = await apiService.getNoticias();
                        break;
                    case 'artigos':
                        this.artigos = await apiService.getArtigos();
                        break;
                    case 'editais':
                        this.editais = await apiService.getEditais();
                        break;
                }
                window.scrollTo({ top: 0, behavior: 'smooth' });
            } catch (error) {
                console.error(`Error navigating to ${page}:`, error);
                this.showAlert('danger', `Erro ao carregar a página ${page}.`);
            } finally {
                this.loading = false;
            }
        },
        
        async performSearch() {
            if (!this.searchQuery.trim()) {
                this.showAlert('warning', 'Digite algo para buscar.');
                return;
            }
            try {
                this.loading = true;
                this.lastSearchQuery = this.searchQuery;
                this.searchResults = await apiService.search(this.searchQuery);
                this.currentPage = 'search';
                window.location.hash = 'search';
            } catch (error) {
                console.error('Error performing search:', error);
                this.showAlert('danger', 'Erro ao realizar busca.');
            } finally {
                this.loading = false;
            }
        },
        
        toggleMobileMenu() { this.mobileMenuOpen = !this.mobileMenuOpen; },
        handleLoginSuccess(user) { this.user = user; },
        handleRegisterSuccess(user) { this.user = user; },
        handleProfileUpdated(user) { this.user = user; },
        async logout() {
            const refreshToken = localStorage.getItem('refresh_token');
            try {
                if (refreshToken) {
                    await apiService.call('POST', '/auth/logout/', { refresh: refreshToken });
                }
            } catch (error) {
                console.error('Server-side logout failed:', error);
            } finally {
                localStorage.removeItem('access_token');
                localStorage.removeItem('refresh_token');
                this.user = null;
                this.showAlert('success', 'Logout realizado com sucesso!');
                this.navigateTo('home');
            }
        },
        showAlert(type, message) {
            this.alert = { show: true, type, message };
            setTimeout(() => this.closeAlert(), 5000);
        },
        closeAlert() { this.alert.show = false; },
        getAlertIcon(type) {
            const icons = { success: 'fas fa-check-circle', danger: 'fas fa-exclamation-triangle', warning: 'fas fa-exclamation-circle', info: 'fas fa-info-circle' };
            return icons[type] || icons.info;
        }
    },
    
    components: {
        'home-component': defineAsyncComponent(() => Promise.resolve(window.VueComponents.HomeComponent)),
        'login-component': defineAsyncComponent(() => Promise.resolve(window.VueComponents.LoginComponent)),
        'register-component': defineAsyncComponent(() => Promise.resolve(window.VueComponents.RegisterComponent)),
        'noticias-component': defineAsyncComponent(() => Promise.resolve(window.VueComponents.NoticiasComponent)),
        'artigos-component': defineAsyncComponent(() => Promise.resolve(window.VueAdvancedComponents.ArtigosComponent)),
        'editais-component': defineAsyncComponent(() => Promise.resolve(window.VueAdvancedComponents.EditaisComponent)),
        'noticia-detail-component': defineAsyncComponent(() => Promise.resolve(window.VueAdvancedComponents.NoticiaDetailComponent)),
        'artigo-detail-component': defineAsyncComponent(() => Promise.resolve(window.VueDetailComponents.ArtigoDetailComponent)),
        'edital-detail-component': defineAsyncComponent(() => Promise.resolve(window.VueDetailComponents.EditalDetailComponent)),
        'search-results-component': defineAsyncComponent(() => Promise.resolve(window.VueAdvancedComponents.SearchResultsComponent)),
        'profile-component': defineAsyncComponent(() => Promise.resolve(window.VueAdvancedComponents.ProfileComponent)),
    }
});

app.mount('#app');

window.addEventListener('hashchange', () => {
    const hash = window.location.hash.substring(1).split('/')[0];
    if (app.currentPage !== hash) {
        app.handleRouting();
    }
});

