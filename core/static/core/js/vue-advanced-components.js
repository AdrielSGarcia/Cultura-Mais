const ArtigosComponent = {
    props: ['artigos'],
    emits: ['navigate', 'show-alert'],
    template: `
        <div class="container">
            <div class="row">
                <div class="col-12"><h2 class="section-title"><i class="fas fa-book me-3"></i> Artigos</h2></div>
            </div>
            
            <div class="row" v-if="artigos && artigos.results && artigos.results.length > 0">
                <div v-for="artigo in artigos.results" :key="artigo.id" class="col-lg-6 col-xl-4 mb-4">
                    <!-- ANIMAÇÕES REMOVIDAS DO CARD -->
                    <div class="card h-100">
                        <div class="card-body">
                            <h5 class="card-title"><a href="#" @click.prevent="$emit('navigate', 'artigo-detail', artigo.id)">{{ artigo.titulo }}</a></h5>
                            <p class="card-text">{{ formatContent(artigo.conteudo) }}</p>
                            <div class="content-meta">
                                <i class="fas fa-user"></i> Por {{ artigo.autor ? artigo.autor.username : 'Autor desconhecido' }} <br>
                                <i class="fas fa-calendar"></i> {{ formatDate(artigo.data_publicacao) }} <br>
                                <i class="fas fa-comments"></i> {{ artigo.comentarios_count || 0 }} comentário(s)
                            </div>
                            <a href="#" @click.prevent="$emit('navigate', 'artigo-detail', artigo.id)" class="btn btn-success"><i class="fas fa-arrow-right me-2"></i> Leia mais</a>
                        </div>
                    </div>
                </div>
            </div>
            
            <div v-else class="row">
                <div class="col-12 text-center">
                    <div class="card"><div class="card-body py-5"><i class="fas fa-book fa-5x text-muted mb-4"></i><h4 class="text-muted">Nenhum artigo encontrado</h4><p class="text-muted">Não há artigos disponíveis no momento.</p></div></div>
                </div>
            </div>
        </div>
    `,
    methods: {
        formatContent(content) { return content && content.length > 150 ? content.substring(0, 150) + '...' : content; },
        formatDate(dateString) { return dateString ? new Date(dateString).toLocaleDateString('pt-BR') : ''; }
    }
};

const EditaisComponent = {
    props: ['editais'],
    emits: ['navigate', 'show-alert'],
    template: `
        <div class="container">
            <div class="row">
                <div class="col-12"><h2 class="section-title"><i class="fas fa-file-alt me-3"></i> Editais</h2></div>
            </div>
            
            <div class="row" v-if="editais && editais.results && editais.results.length > 0">
                <div v-for="edital in editais.results" :key="edital.id" class="col-lg-6 col-xl-4 mb-4">
                    <!-- ANIMAÇÕES REMOVIDAS DO CARD -->
                    <div class="card h-100">
                        <div class="card-body">
                            <h5 class="card-title"><a href="#" @click.prevent="$emit('navigate', 'edital-detail', edital.id)">{{ edital.titulo }}</a></h5>
                            <p class="card-text">{{ formatContent(edital.conteudo) }}</p>
                            <div class="content-meta">
                                <i class="fas fa-user"></i> Por {{ edital.autor ? edital.autor.username : 'Autor desconhecido' }} <br>
                                <i class="fas fa-calendar"></i> {{ formatDate(edital.data_publicacao) }} <br>
                                <i class="fas fa-comments"></i> {{ edital.comentarios_count || 0 }} comentário(s) <br>
                                <i class="fas fa-file-download" v-if="edital.arquivo"></i> <span v-if="edital.arquivo">Arquivo disponível</span>
                            </div>
                            <a href="#" @click.prevent="$emit('navigate', 'edital-detail', edital.id)" class="btn btn-secondary"><i class="fas fa-arrow-right me-2"></i> Leia mais</a>
                        </div>
                    </div>
                </div>
            </div>
            
            <div v-else class="row">
                <div class="col-12 text-center">
                    <div class="card"><div class="card-body py-5"><i class="fas fa-file-alt fa-5x text-muted mb-4"></i><h4 class="text-muted">Nenhum edital encontrado</h4><p class="text-muted">Não há editais disponíveis no momento.</p></div></div>
                </div>
            </div>
        </div>
    `,
    methods: {
        formatContent(content) { return content && content.length > 150 ? content.substring(0, 150) + '...' : content; },
        formatDate(dateString) { return dateString ? new Date(dateString).toLocaleDateString('pt-BR') : ''; }
    }
};

const NoticiaDetailComponent = {
    props: ['noticiaId', 'user'],
    emits: ['navigate', 'show-alert'],
    data() { return { noticia: null, comentarios: [], loading: true, commentForm: { conteudo: '' }, submittingComment: false }; },
    async mounted() { await this.loadNoticia(); await this.loadComentarios(); },
    template: `
        <div class="container">
            <div v-if="loading" class="text-center py-5"><div class="spinner-border text-primary" role="status"><span class="visually-hidden">Carregando...</span></div></div>
            
            <div v-else-if="noticia">
                <div class="mb-4"><button class="btn btn-outline-primary" @click="$emit('navigate', 'noticias')"><i class="fas fa-arrow-left me-2"></i> Voltar para Notícias</button></div>
                <article class="card shadow-custom mb-4">
                    <div class="card-body p-4">
                        <h1 class="card-title display-6 mb-4">{{ noticia.titulo }}</h1>
                        <div class="content-meta mb-4">
                            <i class="fas fa-user"></i> Por {{ noticia.autor ? noticia.autor.username : 'Autor desconhecido' }} <br>
                            <i class="fas fa-calendar"></i> {{ formatDate(noticia.data_publicacao) }}
                        </div>
                        <div class="card-text" style="white-space: pre-wrap; line-height: 1.8;">{{ noticia.conteudo }}</div>
                    </div>
                </article>
                <div class="comment-section">
                    <h3 class="mb-4"><i class="fas fa-comments me-2"></i> Comentários ({{ comentarios.length }})</h3>
                    <div v-if="user" class="mb-4">
                        <h5>Adicionar Comentário</h5>
                        <form @submit.prevent="submitComment">
                            <div class="mb-3"><label for="comment-content" class="form-label">Seu comentário:</label><textarea class="form-control" id="comment-content" rows="4" v-model="commentForm.conteudo" required placeholder="Digite seu comentário aqui..."></textarea></div>
                            <button type="submit" class="btn btn-primary" :disabled="submittingComment">
                                <span v-if="submittingComment" class="spinner-border spinner-border-sm me-2"></span>
                                <i v-else class="fas fa-paper-plane me-2"></i>
                                {{ submittingComment ? 'Enviando...' : 'Adicionar Comentário' }}
                            </button>
                        </form>
                    </div>
                    <div v-else class="alert alert-info mb-4"><i class="fas fa-info-circle me-2"></i> Você precisa estar logado para comentar. <a href="#" @click.prevent="$emit('navigate', 'login')" class="alert-link">Faça login</a> ou <a href="#" @click.prevent="$emit('navigate', 'register')" class="alert-link">cadastre-se</a>.</div>
                    <div v-if="comentarios.length > 0">
                        <div v-for="comentario in comentarios" :key="comentario.id" class="comment">
                            <div class="comment-author"><i class="fas fa-user-circle"></i> {{ comentario.autor ? comentario.autor.username : 'Usuário' }}</div>
                            <div class="comment-date"><i class="fas fa-clock"></i> {{ formatDate(comentario.data_publicacao) }}</div>
                            <div class="comment-content">{{ comentario.conteudo }}</div>
                        </div>
                    </div>
                    <div v-else class="text-center text-muted py-4"><i class="fas fa-comments fa-3x mb-3 opacity-25"></i><p>Nenhum comentário ainda. Seja o primeiro a comentar!</p></div>
                </div>
            </div>
            
            <div v-else class="text-center py-5"><div class="card"><div class="card-body"><i class="fas fa-exclamation-triangle fa-3x text-warning mb-3"></i><h4>Notícia não encontrada</h4><p class="text-muted">A notícia que você está procurando não existe ou foi removida.</p><button class="btn btn-primary" @click="$emit('navigate', 'noticias')">Ver Todas as Notícias</button></div></div></div>
        </div>
    `,
    methods: {
        async loadNoticia() {
            try { this.noticia = await apiService.getNoticia(this.noticiaId); } 
            catch (error) { console.error('Error loading noticia:', error); this.$emit('show-alert', 'danger', 'Erro ao carregar notícia.'); } 
            finally { this.loading = false; }
        },
        async loadComentarios() {
            try { this.comentarios = await apiService.getNoticiaComments(this.noticiaId); } 
            catch (error) { console.error('Error loading comments:', error); }
        },
        async submitComment() {
            if (!this.commentForm.conteudo.trim()) { this.$emit('show-alert', 'warning', 'Por favor, digite um comentário.'); return; }
            this.submittingComment = true;
            try {
                await apiService.addNoticiaComment(this.noticiaId, this.commentForm);
                this.commentForm.conteudo = '';
                await this.loadComentarios();
                this.$emit('show-alert', 'success', 'Comentário adicionado com sucesso!');
            } catch (error) {
                console.error('Error submitting comment:', error);
                this.$emit('show-alert', 'danger', 'Erro ao adicionar comentário.');
            } finally {
                this.submittingComment = false;
            }
        },
        formatDate(dateString) {
            if (!dateString) return '';
            const date = new Date(dateString);
            return date.toLocaleDateString('pt-BR', { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' });
        }
    },
    watch: {
        noticiaId: {
            immediate: true,
            async handler(newId) {
                if (newId) { this.loading = true; await this.loadNoticia(); await this.loadComentarios(); }
            }
        }
    }
};

const SearchResultsComponent = {
    props: ['searchResults', 'searchQuery'],
    emits: ['navigate', 'show-alert'],
    template: `
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <h2 class="section-title"><i class="fas fa-search me-3"></i> Resultados da Busca</h2>
                    <p class="lead text-center mb-4">Resultados para: <strong>"{{ searchQuery }}"</strong></p>
                </div>
            </div>
            
            <div v-if="hasResults">
                <div v-if="searchResults.noticias && searchResults.noticias.length > 0" class="mb-5">
                    <h4 class="mb-3"><i class="fas fa-newspaper me-2 text-primary"></i> Notícias ({{ searchResults.noticias.length }})</h4>
                    <div class="row">
                        <div v-for="noticia in searchResults.noticias" :key="'noticia-' + noticia.id" class="col-lg-6 mb-3">
                            <div class="card h-100"><div class="card-body">
                                <h6 class="card-title"><a href="#" @click.prevent="$emit('navigate', 'noticia-detail', noticia.id)">{{ noticia.titulo }}</a></h6>
                                <p class="card-text small">{{ formatContent(noticia.conteudo) }}</p>
                                <small class="text-muted"><i class="fas fa-calendar me-1"></i> {{ formatDate(noticia.data_publicacao) }}</small>
                            </div></div>
                        </div>
                    </div>
                </div>
                <div v-if="searchResults.artigos && searchResults.artigos.length > 0" class="mb-5">
                    <h4 class="mb-3"><i class="fas fa-book me-2 text-success"></i> Artigos ({{ searchResults.artigos.length }})</h4>
                    <div class="row">
                        <div v-for="artigo in searchResults.artigos" :key="'artigo-' + artigo.id" class="col-lg-6 mb-3">
                            <div class="card h-100"><div class="card-body">
                                <h6 class="card-title"><a href="#" @click.prevent="$emit('navigate', 'artigo-detail', artigo.id)">{{ artigo.titulo }}</a></h6>
                                <p class="card-text small">{{ formatContent(artigo.conteudo) }}</p>
                                <small class="text-muted"><i class="fas fa-calendar me-1"></i> {{ formatDate(artigo.data_publicacao) }}</small>
                            </div></div>
                        </div>
                    </div>
                </div>
                <div v-if="searchResults.editais && searchResults.editais.length > 0" class="mb-5">
                    <h4 class="mb-3"><i class="fas fa-file-alt me-2 text-secondary"></i> Editais ({{ searchResults.editais.length }})</h4>
                    <div class="row">
                        <div v-for="edital in searchResults.editais" :key="'edital-' + edital.id" class="col-lg-6 mb-3">
                            <div class="card h-100"><div class="card-body">
                                <h6 class="card-title"><a href="#" @click.prevent="$emit('navigate', 'edital-detail', edital.id)">{{ edital.titulo }}</a></h6>
                                <p class="card-text small">{{ formatContent(edital.conteudo) }}</p>
                                <small class="text-muted"><i class="fas fa-calendar me-1"></i> {{ formatDate(edital.data_publicacao) }}</small>
                            </div></div>
                        </div>
                    </div>
                </div>
            </div>
            <div v-else class="row"><div class="col-12 text-center"><div class="card"><div class="card-body py-5"><i class="fas fa-search fa-5x text-muted mb-4"></i><h4 class="text-muted">Nenhum resultado encontrado</h4><p class="text-muted">Não encontramos nenhum resultado para sua busca. Tente usar palavras-chave diferentes.</p><button class="btn btn-primary" @click="$emit('navigate', 'home')">Voltar ao Início</button></div></div></div></div>
        </div>
    `,
    computed: {
        hasResults() { return (this.searchResults.noticias && this.searchResults.noticias.length > 0) || (this.searchResults.artigos && this.searchResults.artigos.length > 0) || (this.searchResults.editais && this.searchResults.editais.length > 0); }
    },
    methods: {
        formatContent(content) { return content && content.length > 100 ? content.substring(0, 100) + '...' : content; },
        formatDate(dateString) { return dateString ? new Date(dateString).toLocaleDateString('pt-BR') : ''; }
    }
};

const ProfileComponent = {
    props: ['user'],
    emits: ['navigate', 'show-alert', 'profile-updated'],
    data() { return { editMode: false, form: { first_name: '', last_name: '', email: '' }, loading: false }; },
    mounted() { if (this.user) { this.form = { first_name: this.user.first_name || '', last_name: this.user.last_name || '', email: this.user.email || '' }; } },
    template: `
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-md-8 col-lg-6">
                    <div class="card shadow-custom">
                        <div class="card-header bg-gradient-primary text-white text-center"><h4 class="mb-0"><i class="fas fa-user-circle me-2"></i> Meu Perfil</h4></div>
                        <div class="card-body p-4">
                            <div v-if="!editMode" class="text-center">
                                <div class="mb-4"><i class="fas fa-user-circle fa-5x text-primary mb-3"></i><h5>{{ user.first_name }} {{ user.last_name }}</h5><p class="text-muted">@{{ user.username }}</p></div>
                                <div class="row text-start">
                                    <div class="col-12 mb-3"><strong>Nome:</strong> {{ user.first_name || 'Não informado' }}</div>
                                    <div class="col-12 mb-3"><strong>Sobrenome:</strong> {{ user.last_name || 'Não informado' }}</div>
                                    <div class="col-12 mb-3"><strong>E-mail:</strong> {{ user.email || 'Não informado' }}</div>
                                    <div class="col-12 mb-3"><strong>Usuário:</strong> {{ user.username }}</div>
                                </div>
                                <button class="btn btn-primary" @click="editMode = true"><i class="fas fa-edit me-2"></i> Editar Perfil</button>
                            </div>
                            <form v-else @submit.prevent="updateProfile">
                                <div class="mb-3"><label for="first_name" class="form-label">Nome</label><input type="text" class="form-control" id="first_name" v-model="form.first_name"></div>
                                <div class="mb-3"><label for="last_name" class="form-label">Sobrenome</label><input type="text" class="form-control" id="last_name" v-model="form.last_name"></div>
                                <div class="mb-4"><label for="email" class="form-label">E-mail</label><input type="email" class="form-control" id="email" v-model="form.email"></div>
                                <div class="d-flex gap-2">
                                    <button type="submit" class="btn btn-success flex-fill" :disabled="loading">
                                        <span v-if="loading" class="spinner-border spinner-border-sm me-2"></span>
                                        <i v-else class="fas fa-save me-2"></i>
                                        {{ loading ? 'Salvando...' : 'Salvar' }}
                                    </button>
                                    <button type="button" class="btn btn-secondary flex-fill" @click="cancelEdit" :disabled="loading"><i class="fas fa-times me-2"></i> Cancelar</button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `,
    methods: {
        async updateProfile() {
            this.loading = true;
            try {
                const updatedUser = await apiService.updateProfile(this.form);
                this.$emit('profile-updated', updatedUser);
                this.$emit('show-alert', 'success', 'Perfil atualizado com sucesso!');
                this.editMode = false;
            } catch (error) {
                console.error('Error updating profile:', error);
                this.$emit('show-alert', 'danger', 'Erro ao atualizar perfil.');
            } finally {
                this.loading = false;
            }
        },
        cancelEdit() {
            this.editMode = false;
            this.form = { first_name: this.user.first_name || '', last_name: this.user.last_name || '', email: this.user.email || '' };
        }
    },
    watch: {
        user: {
            immediate: true,
            handler(newUser) {
                if (newUser) { this.form = { first_name: newUser.first_name || '', last_name: newUser.last_name || '', email: newUser.email || '' }; }
            }
        }
    }
};

window.VueAdvancedComponents = { ArtigosComponent, EditaisComponent, NoticiaDetailComponent, SearchResultsComponent, ProfileComponent };
