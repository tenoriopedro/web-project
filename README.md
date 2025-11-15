# Django Company Website (Full Stack)

<p align="center">
  <a href="https://www.tenorioteste.com" target="_blank">
    <img src="https://img.shields.io/badge/Ver_Demo_ao_Vivo-www.tenorioteste.com-brightgreen?style=for-the-badge&logo=django" alt="Live Demo">
  </a>
</p>

Um website corporativo full-stack e pronto para produção, construído para modernizar a presença digital de uma empresa. O projeto inclui um catálogo de produtos, um sistema de cotação baseado em carrinho e um deploy completo na AWS.

---

### 🚀 Stack Tecnológico & Arquitetura

Este projeto foi construído com foco em boas práticas, desde o desenvolvimento isolado com Docker até um deploy de produção robusto na AWS.

| Área | Tecnologia | Propósito |
| :--- | :--- | :--- |
| **Backend** | Python 3, Django | Lógica de negócio, ORM, Admin |
| **Frontend** | Django Templates, HTML/CSS/JS | Renderização server-side e interatividade |
| **Base de Dados** | PostgreSQL | Base de dados relacional de produção |
| **Dev (Local)** | Docker, Docker Compose | Ambiente de desenvolvimento isolado e replicável |
| **Produção** | AWS EC2 (Ubuntu VM) | Servidor cloud |
| **Servidor Web** | Nginx (Reverse Proxy) | Servir ficheiros estáticos, balanceamento de carga |
| **Servidor App**| Gunicorn (WSGI) | Interface entre o Nginx e a aplicação Django |
| **Segurança** | Certbot (Let's Encrypt) | Gestão e renovação de certificados SSL (HTTPS) |

---

### 🛠️ Funcionalidades Principais

* **Catálogo de Produtos Completo**
    * Gestão de categorias, pesquisa por nome/descrição e paginação.
    * Gestão via Django Admin com otimizações (geração automática de slug, resizing de imagem).

* **Carrinho & Fluxo de Cotação**
    * Gestão de carrinho **baseada em sessão (Session-based)**.
    * Organização de código limpa usando **Class-Based Views (CBV)**.
    * Fluxo de cotação com formulário, gravação em base de dados e envio de email à administração.

* **Formulário de Contacto Seguro**
    * **Validação Server-Side** robusta usando `Django Forms`.
    * Entrega de email configurada via servidor SMTP.
    * Fluxo de redirecionamento (Post-Redirect-Get) para prevenir submissões duplicadas.

* **Design Responsivo**
    * Layout adaptável (mobile-first) com lógica de template modular (`base.html`).
    * UX otimizado (ex: botão de mapa em mobile em vez de mapa incorporado).
