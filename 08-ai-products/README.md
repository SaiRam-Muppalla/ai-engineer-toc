# Stage 8 — AI Product Development

## 🎯 Learning Objectives

By the end of this stage you will:
- Design and build complete AI-powered products
- Understand product thinking for AI applications
- Implement user authentication and subscription billing
- Build SaaS products with freemium models
- Understand AI startup fundamentals
- Launch and grow your AI product

## ⏱️ Estimated Time: 2 weeks

---

## 📐 Key Concepts

### 1. AI Product Design Thinking

**The AI Product Stack:**
```
User Interface (Streamlit / React / Next.js)
       ↓
Business Logic (FastAPI / Django)
       ↓
AI Layer (LLMs / ML Models / RAG)
       ↓
Data Layer (PostgreSQL / Vector DB / Redis)
       ↓
Infrastructure (Docker / Cloud / CI/CD)
```

**Key Questions for Every AI Product:**
1. What problem does it solve? (pain, not a vitamin)
2. Why does it need AI? (not just a CRUD app)
3. Who is the target user?
4. How do you make money?
5. How do you measure success?

### 2. SaaS Monetization Models

| Model | Description | Example |
|-------|-------------|---------|
| Freemium | Free basic, paid premium | Notion AI |
| Usage-based | Pay per API call | OpenAI API |
| Subscription | Monthly/yearly flat fee | GitHub Copilot |
| Per-seat | Pay per team member | Jasper AI |
| Enterprise | Custom pricing | Large RAG systems |

### 3. Full-Stack AI Product Architecture

```
Frontend (Next.js / React)
    ↓
Auth (Clerk / Auth.js / Supabase)
    ↓
API (FastAPI / Next.js API routes)
    ↓
AI Services (OpenAI / HuggingFace / Custom models)
    ↓
Database (Supabase / PostgreSQL / Neon)
    ↓
Vector DB (Pinecone / Chroma / pgvector)
    ↓
Payments (Stripe)
    ↓
Deployment (Vercel + Railway + Modal)
```

### 4. AI Startup Fundamentals

- **Build in public** — Share progress on Twitter/LinkedIn
- **Start with one use case** — Do not boil the ocean
- **Validate before building** — Talk to 10 potential users first
- **Distribution > product** — How will you get users?
- **Pricing psychology** — Most AI SaaS charges $20–$50/month
- **Token cost management** — Understand your AI cost per request

### 5. Rapid AI Product Stack (2024)

| Layer | Tools |
|-------|-------|
| Frontend | Next.js, Vercel |
| Backend | FastAPI, Supabase |
| Auth | Clerk, Supabase Auth |
| AI | OpenAI, Groq, Together AI |
| Vector DB | Pinecone, pgvector |
| Payments | Stripe |
| Email | Resend, SendGrid |
| Analytics | PostHog, Plausible |
| Deployment | Vercel + Railway |

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| FastAPI / Next.js | Backend API |
| Streamlit / React | Frontend |
| Supabase | Database + Auth + Storage |
| Stripe | Payments |
| Clerk | Authentication |
| Vercel | Frontend deployment |
| Railway / Render | Backend deployment |
| Modal / RunPod | GPU functions |

---

## 📚 Resources

See [resources.md](./resources.md) for full list.

| Resource | Type | Link |
|----------|------|-------|
| Y Combinator Startup School | Free Course | https://www.startupschool.org/ |
| Indie Hackers Community | Community | https://www.indiehackers.com/ |
| Build in Public Handbook | Guide | https://buildinpublic.xyz/ |
| Stripe Docs | Official | https://stripe.com/docs |
| Supabase Docs | Official | https://supabase.com/docs |

---

## 🏋️ Exercises

See the [exercises/](./exercises/) folder for:
- `01_product_design.md` — Product design exercises for AI products
- `02_stripe_integration.ipynb` — Add Stripe subscriptions to FastAPI
- `03_user_auth.ipynb` — Add authentication to your AI app

---

## 🛠️ Mini Projects

1. **Landing Page** — Build a landing page for your AI product (with waitlist)
2. **Stripe Integration** — Add subscription billing to an AI app
3. **Analytics Dashboard** — Track product usage with PostHog

---

## 🏆 Major Project

### Build and Launch Your AI SaaS

Build a complete, monetizable AI product and get your first paying user.

**Project Examples:**
- AI writing assistant for a specific niche (lawyers, developers, marketers)
- AI-powered analytics tool for a specific industry
- AI tutoring platform for a specific subject
- AI productivity tool for remote teams

**Requirements:**
- Live URL (not just localhost)
- User authentication
- At least one paid plan (Stripe)
- 10+ beta users
- Documented user feedback and iterations

**Deliverables:**
- GitHub repository
- Live product URL
- 5-minute demo video
- One-page product write-up

---

## ✅ Stage Completion Checklist

- [ ] Designed a product concept with problem, user, and monetization
- [ ] Validated the idea with at least 5 potential users
- [ ] Built an MVP with auth and basic AI functionality
- [ ] Added Stripe payments
- [ ] Deployed to production
- [ ] Acquired at least 10 beta users
- [ ] Documented learnings and iterations

**Next Stage → [09 Career Preparation](../09-career-preparation/)**
