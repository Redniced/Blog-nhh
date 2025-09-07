# Blog-nhh
Creating a blog for myself. Just to get used to coding again:

File structure:
my-blog/
│
├── backend/                  # Flask + Python backend
│   ├── app.py                # Main Flask application
│   ├── config.py             # Configuration settings
│   ├── models/               # MongoDB models (using PyMongo or similar)
│   │   └── post.py
│   ├── routes/               # Flask route handlers
│   │   ├── blog_routes.py
│   │   └── auth_routes.py
│   ├── services/             # Business logic (e.g., CRUD operations)
│   │   └── post_service.py
│   ├── static/               # Static files served by Flask (if needed)
│   └── templates/            # Jinja2 templates (optional if Svelte handles frontend)
│
├── frontend/                 # Svelte frontend
│   ├── public/               # Static assets (favicon, images, etc.)
│   ├── src/
│   │   ├── routes/           # Svelte pages
│   │   │   ├── index.svelte
│   │   │   └── post/[id].svelte
│   │   ├── components/       # Reusable UI components
│   │   ├── stores/           # Svelte stores for state management
│   │   └── lib/              # Utility functions
│   ├── svelte.config.js
│   └── package.json
│
├── database/                 # MongoDB setup and seed scripts
│   └── init_db.py
│
├── .env                      # Environment variables
├── README.md
└── requirements.txt          # Python dependencies