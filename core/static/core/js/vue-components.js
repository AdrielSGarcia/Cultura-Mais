const apiService = {
    baseURL: '/api',
    getAuthHeaders() {
        const token = localStorage.getItem('access_token');
        return token ? { 'Authorization': `Bearer ${token}` } : {};
    },
    async call(method, endpoint, data = null) {
        try {
            const config = {
                method,
                url: `${this.baseURL}${endpoint}`,
                headers: {
                    'Content-Type': 'application/json',
                    ...this.getAuthHeaders()
                }
            };
            if (data) { config.data = data; }
            const response = await axios(config);
            return response.data;
        } catch (error) {
            console.error('API Error:', error.response || error.message);
            throw error;
        }
    },
    login(credentials) { return this.call('POST', '/auth/login/', credentials); },
    register(userData) { return this.call('POST', '/auth/register/', userData); },
    getProfile() { return this.call('GET', '/auth/profile/'); },
    updateProfile(userData) { return this.call('PUT', '/auth/profile/', userData); },
    
    getHomeData() { return this.call('GET', '/home/'); },
    getNoticias() { return this.call('GET', '/noticias/'); },
    getNoticia(id) { return this.call('GET', `/noticias/${id}/`); },
    getNoticiaComments(id) { return this.call('GET', `/noticias/${id}/comentarios/`); },
    addNoticiaComment(id, comment) { return this.call('POST', `/noticias/${id}/adicionar_comentario/`, comment); },
    getArtigos() { return this.call('GET', '/artigos/'); },
    getArtigo(id) { return this.call('GET', `/artigos/${id}/`); },
    getArtigoComments(id) { return this.call('GET', `/artigos/${id}/comentarios/`); },
    addArtigoComment(id, comment) { return this.call('POST', `/artigos/${id}/adicionar_comentario/`, comment); },
    getEditais() { return this.call('GET', '/editais/'); },
    getEdital(id) { return this.call('GET', `/editais/${id}/`); },
    getEditalComments(id) { return this.call('GET', `/editais/${id}/comentarios/`); },
    addEditalComment(id, comment) { return this.call('POST', `/editais/${id}/adicionar_comentario/`, comment); },
    
    search(query) { return this.call('GET', `/search/?q=${encodeURIComponent(query)}`); }
};

const HomeComponent = {
    props: ['homeData'],
    emits: ['navigate', 'show-alert'],
    template: `
        <div>
            <!-- Hero Section -->
            <section class="hero-section">
                <div class="container">
                    <div class="row align-items-center">
                        <div class="col-lg-8">
                            <!-- ANIMAÇÕES REMOVIDAS -->
                            <h1>Bem-vindo ao Cultura Mais</h1>
                            <p class="lead">
                                Seu portal de informações culturais. Descubra as últimas notícias, 
                                artigos e editais do mundo da cultura.
                            </p>
                            <div>
                                <button class="btn btn-light btn-lg me-3" @click="$emit('navigate', 'noticias')">
                                    <i class="fas fa-newspaper me-2"></i> Explorar Notícias
                                </button>
                                <button class="btn btn-outline-light btn-lg" @click="$emit('navigate', 'artigos')">
                                    <i class="fas fa-book me-2"></i> Ver Artigos
                                </button>
                            </div>
                        </div>
                        <div class="col-lg-4 text-center">
                             <div><i class="fas fa-palette" style="font-size: 8rem; opacity: 0.3;"></i></div>
                        </div>
                    </div>
                </div>
            </section>

            <div class="container">
                <div class="row">
                    <!-- Latest News -->
                    <div class="col-lg-4 mb-4">
                        <div class="card h-100">
                            <div class="card-header bg-gradient-primary text-white">
                                <h5 class="mb-0"><i class="fas fa-newspaper me-2"></i> Últimas Notícias</h5>
                            </div>
                            <div class="card-body">
                                <div v-if="homeData.ultimas_noticias && homeData.ultimas_noticias.length > 0">
                                    <div v-for="noticia in homeData.ultimas_noticias" :key="noticia.id" class="mb-3 pb-3 border-bottom">
                                        <h6><a href="#" @click.prevent="$emit('navigate', 'noticia-detail', noticia.id)">{{ noticia.titulo }}</a></h6>
                                        <p class="card-text small text-muted">{{ formatContent(noticia.conteudo) }}</p>
                                        <small class="text-muted"><i class="fas fa-calendar me-1"></i> {{ formatDate(noticia.data_publicacao) }}</small>
                                    </div>
                                </div>
                                <div v-else class="text-center text-muted"><i class="fas fa-newspaper fa-3x mb-3 opacity-25"></i><p>Nenhuma notícia disponível</p></div>
                                <div class="text-center mt-3">
                                    <button class="btn btn-outline-primary" @click="$emit('navigate', 'noticias')">Ver Todas as Notícias</button>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Latest Articles -->
                    <div class="col-lg-4 mb-4">
                        <div class="card h-100">
                            <div class="card-header bg-gradient-success text-white">
                                <h5 class="mb-0"><i class="fas fa-book me-2"></i> Últimos Artigos</h5>
                            </div>
                            <div class="card-body">
                                <div v-if="homeData.ultimos_artigos && homeData.ultimos_artigos.length > 0">
                                    <div v-for="artigo in homeData.ultimos_artigos" :key="artigo.id" class="mb-3 pb-3 border-bottom">
                                        <h6><a href="#" @click.prevent="$emit('navigate', 'artigo-detail', artigo.id)">{{ artigo.titulo }}</a></h6>
                                        <p class="card-text small text-muted">{{ formatContent(artigo.conteudo) }}</p>
                                        <small class="text-muted"><i class="fas fa-calendar me-1"></i> {{ formatDate(artigo.data_publicacao) }}</small>
                                    </div>
                                </div>
                                <div v-else class="text-center text-muted"><i class="fas fa-book fa-3x mb-3 opacity-25"></i><p>Nenhum artigo disponível</p></div>
                                <div class="text-center mt-3">
                                    <button class="btn btn-outline-success" @click="$emit('navigate', 'artigos')">Ver Todos os Artigos</button>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Latest Editais -->
                    <div class="col-lg-4 mb-4">
                        <div class="card h-100">
                            <div class="card-header bg-gradient-secondary text-white">
                                <h5 class="mb-0"><i class="fas fa-file-alt me-2"></i> Últimos Editais</h5>
                            </div>
                            <div class="card-body">
                                <div v-if="homeData.ultimos_editais && homeData.ultimos_editais.length > 0">
                                    <div v-for="edital in homeData.ultimos_editais" :key="edital.id" class="mb-3 pb-3 border-bottom">
                                        <h6><a href="#" @click.prevent="$emit('navigate', 'edital-detail', edital.id)">{{ edital.titulo }}</a></h6>
                                        <p class="card-text small text-muted">{{ formatContent(edital.conteudo) }}</p>
                                        <small class="text-muted"><i class="fas fa-calendar me-1"></i> {{ formatDate(edital.data_publicacao) }}</small>
                                    </div>
                                </div>
                                <div v-else class="text-center text-muted"><i class="fas fa-file-alt fa-3x mb-3 opacity-25"></i><p>Nenhum edital disponível</p></div>
                                <div class="text-center mt-3">
                                    <button class="btn btn-outline-secondary" @click="$emit('navigate', 'editais')">Ver Todos os Editais</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `,
    methods: {
        formatContent(content) { return content && content.length > 100 ? content.substring(0, 100) + '...' : content; },
        formatDate(dateString) { return dateString ? new Date(dateString).toLocaleDateString('pt-BR') : ''; }
    }
};

const NoticiasComponent = {
    props: ['noticias'],
    emits: ['navigate', 'show-alert'],
    template: `
        <div class="container">
            <div class="row">
                <div class="col-12"><h2 class="section-title"><i class="fas fa-newspaper me-3"></i> Notícias</h2></div>
            </div>
            
            <div class="row" v-if="noticias && noticias.results && noticias.results.length > 0">
                <div v-for="noticia in noticias.results" :key="noticia.id" class="col-lg-6 col-xl-4 mb-4">
                    <!-- ANIMAÇÕES REMOVIDAS DO CARD -->
                    <div class="card h-100">
                        <div class="card-body">
                            <h5 class="card-title"><a href="#" @click.prevent="$emit('navigate', 'noticia-detail', noticia.id)">{{ noticia.titulo }}</a></h5>
                            <p class="card-text">{{ formatContent(noticia.conteudo) }}</p>
                            <div class="content-meta">
                                <i class="fas fa-user"></i> Por {{ noticia.autor ? noticia.autor.username : 'Autor desconhecido' }} <br>
                                <i class="fas fa-calendar"></i> {{ formatDate(noticia.data_publicacao) }} <br>
                                <i class="fas fa-comments"></i> {{ noticia.comentarios_count || 0 }} comentário(s)
                            </div>
                            <a href="#" @click.prevent="$emit('navigate', 'noticia-detail', noticia.id)" class="btn btn-primary"><i class="fas fa-arrow-right me-2"></i> Leia mais</a>
                        </div>
                    </div>
                </div>
            </div>
            
            <div v-else class="row">
                <div class="col-12 text-center">
                    <div class="card"><div class="card-body py-5"><i class="fas fa-newspaper fa-5x text-muted mb-4"></i><h4 class="text-muted">Nenhuma notícia encontrada</h4><p class="text-muted">Não há notícias disponíveis no momento.</p></div></div>
                </div>
            </div>
        </div>
    `,
    methods: {
        formatContent(content) { return content && content.length > 150 ? content.substring(0, 150) + '...' : content; },
        formatDate(dateString) { return dateString ? new Date(dateString).toLocaleDateString('pt-BR') : ''; }
    }
};

const LoginComponent = {
    emits: ['login-success', 'navigate', 'show-alert'],
    data() { return { form: { username: '', password: '' }, loading: false }; },
    template: `
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-md-6 col-lg-4">
                    <div class="card shadow-custom">
                        <div class="card-header bg-gradient-primary text-white text-center"><h4 class="mb-0"><i class="fas fa-sign-in-alt me-2"></i> Entrar</h4></div>
                        <div class="card-body p-4">
                            <form @submit.prevent="login">
                                <div class="mb-3"><label for="username" class="form-label">Usuário</label><input type="text" class="form-control" id="username" v-model="form.username" required></div>
                                <div class="mb-4"><label for="password" class="form-label">Senha</label><input type="password" class="form-control" id="password" v-model="form.password" required></div>
                                <button type="submit" class="btn btn-primary w-100" :disabled="loading">
                                    <span v-if="loading" class="spinner-border spinner-border-sm me-2"></span>
                                    <i v-else class="fas fa-sign-in-alt me-2"></i>
                                    {{ loading ? 'Entrando...' : 'Entrar' }}
                                </button>
                            </form>
                            <div class="text-center mt-3"><p class="mb-0">Não tem uma conta? <a href="#" @click.prevent="$emit('navigate', 'register')" class="text-primary">Cadastre-se</a></p></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `,
    methods: {
        async login() {
            this.loading = true;
            try {
                const response = await apiService.login(this.form);
                localStorage.setItem('access_token', response.access);
                localStorage.setItem('refresh_token', response.refresh);
                this.$emit('login-success', response.user);
                this.$emit('show-alert', 'success', 'Login realizado com sucesso!');
                this.$emit('navigate', 'home');
            } catch (error) {
                this.$emit('show-alert', 'danger', 'Erro ao fazer login. Verifique suas credenciais.');
            } finally {
                this.loading = false;
            }
        }
    }
};

const RegisterComponent = {
    emits: ['register-success', 'navigate', 'show-alert'],
    data() { return { form: { username: '', email: '', first_name: '', last_name: '', password: '', password_confirm: '' }, loading: false }; },
    template: `
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-md-8 col-lg-6">
                    <div class="card shadow-custom">
                        <div class="card-header bg-gradient-success text-white text-center"><h4 class="mb-0"><i class="fas fa-user-plus me-2"></i> Cadastrar</h4></div>
                        <div class="card-body p-4">
                            <form @submit.prevent="register">
                                <div class="row">
                                    <div class="col-md-6 mb-3"><label for="first_name" class="form-label">Nome</label><input type="text" class="form-control" id="first_name" v-model="form.first_name" required></div>
                                    <div class="col-md-6 mb-3"><label for="last_name" class="form-label">Sobrenome</label><input type="text" class="form-control" id="last_name" v-model="form.last_name" required></div>
                                </div>
                                <div class="mb-3"><label for="username" class="form-label">Usuário</label><input type="text" class="form-control" id="username" v-model="form.username" required></div>
                                <div class="mb-3"><label for="email" class="form-label">E-mail</label><input type="email" class="form-control" id="email" v-model="form.email" required></div>
                                <div class="row">
                                    <div class="col-md-6 mb-3"><label for="password" class="form-label">Senha</label><input type="password" class="form-control" id="password" v-model="form.password" required></div>
                                    <div class="col-md-6 mb-4"><label for="password_confirm" class="form-label">Confirmar Senha</label><input type="password" class="form-control" id="password_confirm" v-model="form.password_confirm" required></div>
                                </div>
                                <button type="submit" class="btn btn-success w-100" :disabled="loading">
                                    <span v-if="loading" class="spinner-border spinner-border-sm me-2"></span>
                                    <i v-else class="fas fa-user-plus me-2"></i>
                                    {{ loading ? 'Cadastrando...' : 'Cadastrar' }}
                                </button>
                            </form>
                            <div class="text-center mt-3"><p class="mb-0">Já tem uma conta? <a href="#" @click.prevent="$emit('navigate', 'login')" class="text-success">Faça login</a></p></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `,
    methods: {
        async register() {
            if (this.form.password !== this.form.password_confirm) {
                this.$emit('show-alert', 'danger', 'As senhas não coincidem.');
                return;
            }
            this.loading = true;
            try {
                const response = await apiService.register(this.form);
                localStorage.setItem('access_token', response.access);
                localStorage.setItem('refresh_token', response.refresh);
                this.$emit('register-success', response.user);
                this.$emit('show-alert', 'success', 'Cadastro realizado com sucesso!');
                this.$emit('navigate', 'home');
            } catch (error) {
                this.$emit('show-alert', 'danger', 'Erro ao fazer cadastro. Tente novamente.');
            } finally {
                this.loading = false;
            }
        }
    }
};

window.VueComponents = { HomeComponent, NoticiasComponent, LoginComponent, RegisterComponent };
