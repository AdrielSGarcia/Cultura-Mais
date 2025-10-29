const ArtigoDetailComponent = {
    props: ['artigoId', 'user'],
    emits: ['navigate', 'show-alert'],
    data() { return { artigo: null, comentarios: [], loading: true, commentForm: { conteudo: '' }, submittingComment: false }; },
    async mounted() { await this.loadArtigo(); await this.loadComentarios(); },
    template: `
        <div class="container">
            <div v-if="loading" class="text-center py-5"><div class="spinner-border text-success" role="status"><span class="visually-hidden">Carregando...</span></div></div>
            
            <div v-else-if="artigo">
                <div class="mb-4"><button class="btn btn-outline-success" @click="$emit('navigate', 'artigos')"><i class="fas fa-arrow-left me-2"></i> Voltar para Artigos</button></div>
                <article class="card shadow-custom mb-4">
                    <div class="card-body p-4">
                        <h1 class="card-title display-6 mb-4">{{ artigo.titulo }}</h1>
                        <div class="content-meta mb-4">
                            <i class="fas fa-user"></i> Por {{ artigo.autor ? artigo.autor.username : 'Autor desconhecido' }} <br>
                            <i class="fas fa-calendar"></i> {{ formatDate(artigo.data_publicacao) }}
                        </div>
                        <div class="card-text" style="white-space: pre-wrap; line-height: 1.8;">{{ artigo.conteudo }}</div>
                    </div>
                </article>
                <div class="comment-section">
                    <h3 class="mb-4"><i class="fas fa-comments me-2"></i> Comentários ({{ comentarios.length }})</h3>
                    <div v-if="user" class="mb-4">
                        <h5>Adicionar Comentário</h5>
                        <form @submit.prevent="submitComment">
                            <div class="mb-3"><label for="comment-content" class="form-label">Seu comentário:</label><textarea class="form-control" id="comment-content" rows="4" v-model="commentForm.conteudo" required placeholder="Digite seu comentário aqui..."></textarea></div>
                            <button type="submit" class="btn btn-success" :disabled="submittingComment">
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
            
            <div v-else class="text-center py-5"><div class="card"><div class="card-body"><i class="fas fa-exclamation-triangle fa-3x text-warning mb-3"></i><h4>Artigo não encontrado</h4><p class="text-muted">O artigo que você está procurando não existe ou foi removido.</p><button class="btn btn-success" @click="$emit('navigate', 'artigos')">Ver Todos os Artigos</button></div></div></div>
        </div>
    `,
    methods: {
        async loadArtigo() {
            try { this.artigo = await apiService.getArtigo(this.artigoId); } 
            catch (error) { console.error('Error loading artigo:', error); this.$emit('show-alert', 'danger', 'Erro ao carregar artigo.'); } 
            finally { this.loading = false; }
        },
        async loadComentarios() {
            try { this.comentarios = await apiService.getArtigoComments(this.artigoId); } 
            catch (error) { console.error('Error loading comments:', error); }
        },
        async submitComment() {
            if (!this.commentForm.conteudo.trim()) { this.$emit('show-alert', 'warning', 'Por favor, digite um comentário.'); return; }
            this.submittingComment = true;
            try {
                await apiService.addArtigoComment(this.artigoId, this.commentForm);
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
        artigoId: {
            immediate: true,
            async handler(newId) {
                if (newId) { this.loading = true; await this.loadArtigo(); await this.loadComentarios(); }
            }
        }
    }
};

const EditalDetailComponent = {
    props: ['editalId', 'user'],
    emits: ['navigate', 'show-alert'],
    data() { return { edital: null, comentarios: [], loading: true, commentForm: { conteudo: '' }, submittingComment: false }; },
    async mounted() { await this.loadEdital(); await this.loadComentarios(); },
    template: `
        <div class="container">
            <div v-if="loading" class="text-center py-5"><div class="spinner-border text-secondary" role="status"><span class="visually-hidden">Carregando...</span></div></div>
            
            <div v-else-if="edital">
                <div class="mb-4"><button class="btn btn-outline-secondary" @click="$emit('navigate', 'editais')"><i class="fas fa-arrow-left me-2"></i> Voltar para Editais</button></div>
                <article class="card shadow-custom mb-4">
                    <div class="card-body p-4">
                        <h1 class="card-title display-6 mb-4">{{ edital.titulo }}</h1>
                        <div class="content-meta mb-4">
                            <i class="fas fa-user"></i> Por {{ edital.autor ? edital.autor.username : 'Autor desconhecido' }} <br>
                            <i class="fas fa-calendar"></i> {{ formatDate(edital.data_publicacao) }} <br>
                            <i class="fas fa-file-download" v-if="edital.arquivo"></i> <span v-if="edital.arquivo"><a :href="edital.arquivo" target="_blank" class="text-primary">Baixar arquivo do edital</a></span>
                        </div>
                        <div class="card-text" style="white-space: pre-wrap; line-height: 1.8;">{{ edital.conteudo }}</div>
                    </div>
                </article>
                <div class="comment-section">
                    <h3 class="mb-4"><i class="fas fa-comments me-2"></i> Comentários ({{ comentarios.length }})</h3>
                    <div v-if="user" class="mb-4">
                        <h5>Adicionar Comentário</h5>
                        <form @submit.prevent="submitComment">
                            <div class="mb-3"><label for="comment-content" class="form-label">Seu comentário:</label><textarea class="form-control" id="comment-content" rows="4" v-model="commentForm.conteudo" required placeholder="Digite seu comentário aqui..."></textarea></div>
                            <button type="submit" class="btn btn-secondary" :disabled="submittingComment">
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
            
            <div v-else class="text-center py-5"><div class="card"><div class="card-body"><i class="fas fa-exclamation-triangle fa-3x text-warning mb-3"></i><h4>Edital não encontrado</h4><p class="text-muted">O edital que você está procurando não existe ou foi removido.</p><button class="btn btn-secondary" @click="$emit('navigate', 'editais')">Ver Todos os Editais</button></div></div></div>
        </div>
    `,
    methods: {
        async loadEdital() {
            try { this.edital = await apiService.getEdital(this.editalId); } 
            catch (error) { console.error('Error loading edital:', error); this.$emit('show-alert', 'danger', 'Erro ao carregar edital.'); } 
            finally { this.loading = false; }
        },
        async loadComentarios() {
            try { this.comentarios = await apiService.getEditalComments(this.editalId); } 
            catch (error) { console.error('Error loading comments:', error); }
        },
        async submitComment() {
            if (!this.commentForm.conteudo.trim()) { this.$emit('show-alert', 'warning', 'Por favor, digite um comentário.'); return; }
            this.submittingComment = true;
            try {
                await apiService.addEditalComment(this.editalId, this.commentForm);
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
        editalId: {
            immediate: true,
            async handler(newId) {
                if (newId) { this.loading = true; await this.loadEdital(); await this.loadComentarios(); }
            }
        }
    }
};

window.VueDetailComponents = { ArtigoDetailComponent, EditalDetailComponent };
