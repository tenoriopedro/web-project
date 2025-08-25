# Django Company Website


This is a company website project built with **Django**, using **Docker** for an isolated environment and **PostgreSQL** as the database. The goal is to create a solid, scalable, and responsive foundation for a corporate website.




## Technologies


- Python 3 + Django  
- PostgreSQL  
- Docker & Docker Compose  
- HTML/CSS/JS (with Django templates)  
- Bash Scripts for automation  
- Django Forms + custom SMTP server  
- AWS EC2 (Ubuntu VM for deployment)  
- Gunicorn + Nginx (production WSGI + reverse proxy)  
- Certbot (HTTPS with Let's Encrypt)


---


## 🛠️ Implemented Features


### ✅ Home Page


The homepage presents the company's identity clearly and responsively. Built with Django templates and based on `base.html`, it ensures consistent layout and modular design. Core components:


- **Hero section** with headline and call-to-action button  
- **Highlights or service blocks** that communicate value  
- **Navigation links** to key pages  
- **Social media icons + floating WhatsApp button** (present across the site)  
- **Fully responsive layout**, including mobile hamburger menu  
- **Semantic HTML and performance-optimized CSS**


### ✅ Contact Page


- **Functional contact form** (Name, Email, Phone, Message)  
- **Server-side validation** using Django Forms  
- **Email delivery via company SMTP server**, with anti-spam protection  
- **Success redirect flow** to prevent duplicate submissions  
- **Visible company contact details** (email, phone, social media, address, hours)  
- **Google Maps link integration** for physical store location  
- **Mobile-specific UX:** map hidden on smaller screens, replaced with a direct Google Maps button


### ✅ Products Page

A products section was implemented to display and organize the company’s catalog (focused on industrial kitchen equipment).  

**Main features:**
- **Categories:** users can choose a product type and view only the relevant items.  
- **Product list with pagination:** navigation is optimized with sorting options (name, id).  
- **Actions available per product:**
  - **Request price via WhatsApp** → sends a pre-filled message directly to the company.  
  - **Add to cart** → integrates with the cart system.  
  - **View details** → opens a dedicated page with extended description and related products.  
- **Search bar:** query by product name, short description, or category.  
- **Admin integration:** management via Django Admin, including image resizing, automatic slug generation, and validation for product setup.  

**Tech highlights:**
- Django Class-Based Views (`ListView`, `DetailView`, `TemplateView`)  
- Custom search with `Q` objects  
- Slug generation + URL structure for SEO-friendly navigation  
- Image upload with automatic resizing  
- Django Admin customization and data validation  

---


## 🚀 Deployment


This project is deployed on **AWS EC2**, running on an **Ubuntu VM**. Key details:


- **Docker** is used **only in development**, not in production.
- In production:
  - App runs via **Gunicorn** (WSGI HTTP server)
  - Served by **Nginx** as a reverse proxy
  - **HTTPS enabled** with **Certbot** and Let's Encrypt
- PostgreSQL is installed directly on the VM (non-Dockerized production database)


---


## 🚧 Progress


- 🌐 Production deployed on AWS EC2 (Ubuntu VM)  
- 🛡️ Secure deployment with HTTPS, Gunicorn, and Nginx
- ✅ Home Page completed  
- ✅ Contact Page completed  
- ✅ Products Page completed
- 🔄 Modular structure with multiple Django apps  
- ⚙️ Automated scripts to simplify development  
- 📦 PostgreSQL database running via Docker (dev)


---


💡 Developed by **Pedro Tenório** • Work in progress 🚧