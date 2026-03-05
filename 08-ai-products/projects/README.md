# Your AI SaaS Project

Build and launch a complete, monetizable AI product.

## 📋 Project Template

### Step 1: Validate Your Idea
Complete the [Product Design Exercise](../exercises/01_product_design.md) first.

### Step 2: Build the MVP

**Minimum requirements for your AI SaaS:**

- [ ] Landing page with clear value proposition
- [ ] User sign-up and login (Clerk or Supabase Auth)
- [ ] Core AI feature (at least one)
- [ ] Subscription billing with Stripe (free + paid tier)
- [ ] Usage limits enforcement
- [ ] Deployed to production (not localhost)
- [ ] Custom domain (optional but professional)

### Step 3: Launch

**Pre-launch checklist:**
- [ ] 5 beta users testing it
- [ ] Feedback incorporated
- [ ] Error tracking set up (Sentry)
- [ ] Analytics set up (PostHog)
- [ ] Support email configured

**Launch channels:**
- [ ] Post on ProductHunt
- [ ] Share in relevant Reddit communities
- [ ] Share in Discord servers
- [ ] Post on LinkedIn with demo video
- [ ] Tweet about it with screenshots

### Step 4: Measure and Iterate

**Key metrics to track:**
| Metric | Target |
|--------|--------|
| Monthly Active Users | 50+ in month 1 |
| Paid Conversion Rate | > 3% |
| Monthly Recurring Revenue | Any amount! |
| Churn Rate | < 20%/month |
| Net Promoter Score | > 30 |

---

## 🏗️ Recommended Tech Stack

```
Frontend:   Next.js + Tailwind CSS → Deploy on Vercel (free)
Backend:    FastAPI → Deploy on Railway or Render (free tier)
Auth:       Clerk (free up to 10k MAU) or Supabase Auth
Database:   Supabase PostgreSQL (free tier: 500MB)
Vector DB:  Pinecone (free tier: 100K vectors)
AI:         OpenAI API / Groq (fast + cheap)
Payments:   Stripe (0% fee until $1M revenue)
Email:      Resend (free: 100 emails/day)
```

---

## 📁 Recommended Project Structure

```
my-ai-saas/
├── frontend/                # Next.js app
│   ├── app/
│   │   ├── (auth)/          # Login/signup pages
│   │   ├── dashboard/       # Main app
│   │   └── api/             # Next.js API routes
│   └── components/
├── backend/                 # FastAPI
│   ├── main.py
│   ├── routers/
│   │   ├── auth.py
│   │   ├── ai.py
│   │   └── billing.py
│   ├── services/
│   │   ├── ai_service.py
│   │   └── stripe_service.py
│   └── models.py
├── docker-compose.yml
└── README.md
```
