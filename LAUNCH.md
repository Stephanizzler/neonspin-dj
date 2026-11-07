# SoundLab DJ: launch checklist

These are the steps that need your own accounts. Everything else is already built.

## 1. Check the name (15 minutes)
- Search "SoundLab DJ" in the App Store, Google Play and on Google.
- Search the trademark databases: USPTO (tmsearch.uspto.gov) and your country's office (e.g. IP Australia or the UK IPO).

## 2. Your own web address: dj.soundlabjr.com (10 minutes, plus up to a day for it to take effect)
1. At your domain provider (where soundlabjr.com is registered), add a DNS record:
   **Type** CNAME · **Name** `dj` · **Value** `stephanizzler.github.io`
2. Tell Claude when that's done. Claude adds the matching `CNAME` file to the site, updates the sharing links, and makes a new QR code.
3. On GitHub: **Settings → Pages → Custom domain** shows `dj.soundlabjr.com`. Tick **Enforce HTTPS** once it's offered.

## 3. Payments with Lemon Squeezy (30 minutes)
1. Sign up at lemonsqueezy.com and set up your store (payout details, tax info).
2. Create one product, "SoundLab DJ Pro", with three variants:
   - Monthly subscription $4.99
   - Yearly subscription $29.99
   - Lifetime (single payment) $49
   Turn on **License keys** for each variant (activation limit about 3 devices).
3. Copy each variant's **checkout link** and your **Store ID** (Settings → Stores).
4. Send them to Claude. Claude pastes them into the app and switches Pro on.
   (In the code this is `PRO_CFG` in index.html: `enforce: true`, `storeId`, and the three `checkout` links.)
5. Test with Lemon Squeezy's test mode before going live.

## 4. Visitor stats (10 minutes, free)
- Sign up at goatcounter.com (free, privacy-friendly, no cookie banner needed) and pick a code, e.g. `soundlabdj`.
- Send Claude the code, and Claude adds the snippet.

## 5. Tell people
- Post the promo videos (in `promo/`): vertical for TikTok, Reels and Shorts; 16:9 for YouTube.
- Share the link. The sharing preview image and text show up automatically.
- Post in DJ communities (e.g. Reddit r/Beatmatch, r/DJs), on Product Hunt, and to your school's families.
- After a couple of weeks, look at the visitor stats and see which features people use. Then switch Pro on.
