import { useState, useEffect, useRef, useCallback } from "react";

// ─── Content Data ─────────────────────────────────────────────────
const NEWS_POSTS = [
  {
    id: 1,
    category: "CAVC Decision",
    date: "Mar 4, 2026",
    title: "Euzebio v. McDonough: What It Means for Your TDIU Claim",
    excerpt: "A breakdown of the latest CAVC ruling and how it could affect veterans currently pursuing Total Disability based on Individual Unemployability. The Court found that VA must consider all evidence of employability, not just the most recent exam.",
    author: "Chris Combs",
    readTime: "8 min",
    featured: true,
    tags: ["CAVC", "TDIU", "Precedent"],
    body: "The Court of Appeals for Veterans Claims issued a significant decision in Euzebio v. McDonough that reshapes how TDIU claims must be evaluated. At its core, the Court held that the Board of Veterans' Appeals erred when it relied solely on a single VA examination to deny TDIU, while disregarding lay evidence and vocational assessments that supported unemployability.\n\nThis matters because many veterans have their TDIU claims denied based on a brief C&P exam that doesn't capture the full picture of how their service-connected disabilities affect their ability to work. The Euzebio decision reinforces that VA must weigh ALL competent evidence — including the veteran's own testimony about their functional limitations.\n\nKey takeaways for practitioners:\n\n• VA cannot cherry-pick a single exam over contradicting evidence\n• Lay statements about work capacity carry real evidentiary weight\n• Vocational expert opinions should be obtained and submitted\n• The \"substantially gainful employment\" standard requires a holistic analysis\n\nIf you have a pending TDIU claim or a recent denial, review whether the decision adequately addressed all evidence of unemployability. This case gives you strong ground for a supplemental claim or Board appeal.",
  },
  {
    id: 2,
    category: "Regulation Update",
    date: "Feb 28, 2026",
    title: "38 CFR § 4.10 Medication Rule: The Ingram v. Collins Saga",
    excerpt: "The ongoing battle over how VA rates disabilities managed by medication — and why every VSO and attorney needs to understand this evolving standard.",
    author: "Chris Combs",
    readTime: "12 min",
    featured: false,
    tags: ["38 CFR", "Ratings", "Medication"],
    body: "One of the most consequential regulatory battles in veterans law right now centers on a deceptively simple question: should VA rate a disability based on how the veteran functions WITH medication, or WITHOUT it?\n\nThe answer has massive implications. A veteran whose hypertension is controlled by daily medication might present with normal blood pressure at a C&P exam — but without that medication, their condition could be severely disabling.\n\nThe Ingram v. Collins line of cases has been pushing VA to confront this issue head-on. Here's what you need to know about the current state of play and how it affects your claims strategy.",
  },
  {
    id: 3,
    category: "Claims Strategy",
    date: "Feb 20, 2026",
    title: "Building a Bulletproof Nexus Letter: AI-Assisted Research",
    excerpt: "How to leverage AI research tools to identify the strongest medical and legal evidence for your veteran clients' nexus letters.",
    author: "Chris Combs",
    readTime: "10 min",
    featured: false,
    tags: ["Nexus", "Evidence", "Strategy"],
    body: "A nexus letter can make or break a VA disability claim. It's the critical link between a veteran's current condition and their military service. But too many nexus letters fail because they lack specificity, don't address the right legal standard, or miss key supporting evidence.\n\nHere's how to use AI research tools to build nexus letters that actually hold up under VA scrutiny.",
  },
  {
    id: 4,
    category: "BVA Analysis",
    date: "Feb 14, 2026",
    title: "BVA Grant Rates by Issue Type: 2025 Data Deep Dive",
    excerpt: "Analyzing Board of Veterans' Appeals decision patterns to identify which claim types see the highest success rates at the Board level.",
    author: "Chris Combs",
    readTime: "15 min",
    featured: false,
    tags: ["BVA", "Data", "Appeals"],
    body: "Understanding BVA grant rates can fundamentally change how you approach a veteran's appeal strategy. Not all claim types are created equal at the Board level — some issues have significantly higher success rates than others, and knowing these patterns gives you a strategic advantage.",
  },
  {
    id: 5,
    category: "VSO Toolkit",
    date: "Feb 7, 2026",
    title: "M21-1 Updates You Missed: January 2026 Changes Decoded",
    excerpt: "A plain-language summary of the latest M21-1 adjudication manual changes and their practical impact on pending claims.",
    author: "Chris Combs",
    readTime: "6 min",
    featured: false,
    tags: ["M21-1", "Policy", "Updates"],
    body: "VA quietly updated several sections of the M21-1 adjudication manual in January 2026. These changes affect how raters evaluate certain conditions and process specific claim types. Here's what changed and what it means for your pending claims.",
  },
  {
    id: 6,
    category: "Know Your Rights",
    date: "Jan 30, 2026",
    title: "The Duty to Assist: What VA Owes You (And What to Do When They Fail)",
    excerpt: "VA has a legal obligation to help develop your claim. Here's what that means in practice, how to spot violations, and how to use them on appeal.",
    author: "Chris Combs",
    readTime: "9 min",
    featured: false,
    tags: ["Rights", "Appeals", "Strategy"],
    body: "One of the most powerful tools in a veteran's arsenal is the VA's duty to assist. Under 38 U.S.C. § 5103A, VA is legally required to make reasonable efforts to help you obtain evidence needed to substantiate your claim. When they fail in this duty, it can be grounds for remand on appeal.",
  },
  {
    id: 7,
    category: "Explainer",
    date: "Jan 22, 2026",
    title: "VA Math Explained: Why 50% + 30% Doesn't Equal 80%",
    excerpt: "The combined ratings table confuses almost every veteran. Here's a plain-English guide to how VA calculates your overall disability percentage.",
    author: "Chris Combs",
    readTime: "5 min",
    featured: false,
    tags: ["Ratings", "Explainer", "Basics"],
    body: "If you've ever been told your combined VA disability rating and thought 'that math doesn't add up,' you're not alone. VA uses a specific formula called the 'combined ratings table' that works nothing like regular addition. Understanding this system is essential for every veteran.",
  },
  {
    id: 8,
    category: "Claims Strategy",
    date: "Jan 15, 2026",
    title: "Secondary Service Connection: The Claims Strategy Most Veterans Miss",
    excerpt: "Your service-connected condition may entitle you to additional ratings for secondary conditions. Here's how to identify and file these claims effectively.",
    author: "Chris Combs",
    readTime: "11 min",
    featured: false,
    tags: ["Secondary", "Strategy", "Ratings"],
    body: "Secondary service connection is one of the most underutilized paths to a higher combined rating. If a service-connected condition causes or aggravates another condition, that secondary condition can also be service-connected under 38 CFR § 3.310.",
  },
];

const QUICK_GUIDES = [
  { icon: "📋", title: "Filing Your First Claim", desc: "Step-by-step from DD-214 to decision letter" },
  { icon: "🏥", title: "C&P Exam Survival Guide", desc: "What to expect, bring, and say at your exam" },
  { icon: "📊", title: "Understanding VA Math", desc: "How combined ratings actually work" },
  { icon: "⚖️", title: "Appeals 101", desc: "HLR, Supplemental, or Board — which lane to pick" },
  { icon: "🔄", title: "Increase Claims", desc: "When and how to file for a higher rating" },
  { icon: "💼", title: "TDIU Explained", desc: "Getting 100% pay without a 100% rating" },
  { icon: "🩺", title: "Nexus Letters", desc: "What makes a nexus letter actually work" },
  { icon: "📝", title: "Buddy Statements", desc: "How lay evidence can strengthen your claim" },
];

const AI_TOOLS = [
  { name: "BVA Decision Search", desc: "Search thousands of Board decisions by keyword, issue, or outcome.", status: "Live" },
  { name: "CAVC Case Analyzer", desc: "Detailed breakdowns of Court decisions — holdings, reasoning, practical impact.", status: "Live" },
  { name: "38 CFR Navigator", desc: "Ask plain-language questions, get the exact regulation sections you need.", status: "Live" },
  { name: "KnowVA / M21-1 Search", desc: "Search VA's adjudication manual to see how raters evaluate your claim type.", status: "Live" },
  { name: "Claims Research Assistant", desc: "AI research system cross-referencing BVA decisions, CAVC precedent, and CFR.", status: "Beta" },
];

// ─── Icons ────────────────────────────────────────────────────────
const ArrowRight = ({ size = 14 }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round">
    <line x1="5" y1="12" x2="19" y2="12" /><polyline points="12 5 19 12 12 19" />
  </svg>
);
const ArrowLeft = ({ size = 14 }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round">
    <line x1="19" y1="12" x2="5" y2="12" /><polyline points="12 19 5 12 12 5" />
  </svg>
);
const MenuIcon = () => (
  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
    <line x1="3" y1="7" x2="21" y2="7" /><line x1="3" y1="12" x2="21" y2="12" /><line x1="3" y1="17" x2="21" y2="17" />
  </svg>
);
const CloseIcon = () => (
  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
    <line x1="18" y1="6" x2="6" y2="18" /><line x1="6" y1="6" x2="18" y2="18" />
  </svg>
);
const SendIcon = () => (
  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z" /></svg>
);
const ClockIcon = () => (
  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
    <circle cx="12" cy="12" r="10" /><polyline points="12 6 12 12 16 14" />
  </svg>
);
const ChevronDown = () => (
  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5"><polyline points="6 9 12 15 18 9" /></svg>
);
const BookIcon = () => (
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
    <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>
  </svg>
);

// ─── Styles ───────────────────────────────────────────────────────
const globalCSS = `
  @import url('https://fonts.googleapis.com/css2?family=Lora:wght@400;500;600;700&family=Source+Sans+3:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

  :root {
    --navy-900: #0B1A2E;
    --navy-800: #0F2240;
    --navy-700: #15305A;
    --navy-600: #1C3E72;
    --gold-500: #C8A232;
    --gold-400: #D9B844;
    --gold-300: #E8CC6A;
    --cream: #FAFAF5;
    --cream-warm: #F5F2EA;
    --cream-border: #E8E4D8;
    --ink: #1A1D26;
    --ink-light: #4A4D5A;
    --ink-muted: #8A8D9A;
    --white: #ffffff;
    --radius: 10px;
    --max-w: 720px;
    --pad: 20px;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
  html { scroll-behavior: smooth; -webkit-text-size-adjust: 100%; }
  body { font-family: 'Source Sans 3', -apple-system, sans-serif; background: var(--cream); color: var(--ink); }
  ::selection { background: rgba(200,162,50,0.25); }

  @keyframes fadeUp { from { opacity:0; transform:translateY(16px); } to { opacity:1; transform:translateY(0); } }
  @keyframes fadeIn { from { opacity:0; } to { opacity:1; } }
  @keyframes slideUp { from { opacity:0; transform:translateY(100%); } to { opacity:1; transform:translateY(0); } }
  @keyframes dotPulse { 0%,60%,100% { opacity:.3; } 30% { opacity:1; } }

  button, a { min-height: 44px; display: inline-flex; align-items: center; }
  .hide-scroll::-webkit-scrollbar { display: none; }
  .hide-scroll { -ms-overflow-style: none; scrollbar-width: none; }

  @media (min-width: 768px) { :root { --pad: 32px; --max-w: 800px; } }
  @media (min-width: 1024px) { :root { --pad: 40px; --max-w: 960px; } }
`;

// ─── Main Component ───────────────────────────────────────────────
export default function V2VSite() {
  const [mobileMenu, setMobileMenu] = useState(false);
  const [activeArticle, setActiveArticle] = useState(null);
  const [selectedTag, setSelectedTag] = useState(null);
  const [showChat, setShowChat] = useState(false);
  const [chatMsgs, setChatMsgs] = useState([
    { role: "ai", text: "Welcome to the V2V Research Assistant. I can search BVA decisions, look up CAVC precedent, navigate 38 CFR, and help with claims strategy. What can I help you research?" }
  ]);
  const [chatInput, setChatInput] = useState("");
  const [typing, setTyping] = useState(false);
  const [expandedTool, setExpandedTool] = useState(null);
  const chatEnd = useRef(null);

  useEffect(() => { chatEnd.current?.scrollIntoView({ behavior: "smooth" }); }, [chatMsgs]);

  const allTags = [...new Set(NEWS_POSTS.flatMap(p => p.tags))];
  const filtered = selectedTag ? NEWS_POSTS.filter(p => p.tags.includes(selectedTag)) : NEWS_POSTS;

  const openArticle = (post) => {
    setActiveArticle(post);
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  const handleChat = useCallback(() => {
    if (!chatInput.trim()) return;
    const q = chatInput.trim();
    setChatMsgs(p => [...p, { role: "user", text: q }]);
    setChatInput("");
    setTyping(true);
    setTimeout(() => {
      const l = q.toLowerCase();
      let r = "";
      if (l.includes("tdiu") || l.includes("unemployab")) r = "TDIU allows veterans to receive 100% compensation even without a 100% combined rating. Key thresholds: one disability at 60%+ OR combined 70%+ with one at 40%+. The recent Euzebio decision strengthened the evidentiary standard — VA must consider ALL evidence of unemployability. Want me to search BVA decisions for TDIU grants?";
      else if (l.includes("bva") || l.includes("board")) r = "I can search our database of 50,000+ BVA decisions by keyword, diagnostic code, or outcome. What issue or condition would you like me to look up?";
      else if (l.includes("cavc") || l.includes("court")) r = "CAVC reviews BVA decisions and sets binding precedent. Notable recent cases include Euzebio v. McDonough (TDIU evidence) and Ingram v. Collins (medication rule). Which case or issue interests you?";
      else if (l.includes("nexus")) r = "A strong nexus letter needs: a clear diagnosis, an \"at least as likely as not\" opinion connecting it to service, and specific rationale citing service records and medical literature. I can search BVA decisions where nexus evidence was decisive — want me to look?";
      else if (l.includes("38 cfr") || l.includes("regulation") || l.includes("cfr")) r = "I can search Title 38 CFR for you. Part 3 covers adjudication rules (claims processing, service connection standards). Part 4 is the rating schedule with diagnostic codes. What topic or section number?";
      else if (l.includes("secondary")) r = "Secondary service connection under 38 CFR § 3.310 allows you to claim conditions caused or aggravated by an already service-connected disability. Common examples: depression secondary to chronic pain, radiculopathy secondary to back conditions. Want me to search BVA grants for specific secondary conditions?";
      else r = `I can research that for you across several databases:\n\n• BVA Decisions — Board rulings related to your topic\n• CAVC Precedent — Court decisions with binding authority\n• 38 CFR — Applicable regulations\n• M21-1 / KnowVA — VA's internal adjudication guidance\n\nWhich source should I search first?`;
      setChatMsgs(p => [...p, { role: "ai", text: r }]);
      setTyping(false);
    }, 1000 + Math.random() * 600);
  }, [chatInput]);

  // ── Article View ────────────────────────────────────────────────
  if (activeArticle) {
    return (
      <>
        <style>{globalCSS}</style>
        <div style={{ minHeight: "100vh", background: "var(--cream)" }}>
          <nav style={{
            position: "sticky", top: 0, zIndex: 50,
            background: "rgba(250,250,245,0.95)", backdropFilter: "blur(10px)",
            borderBottom: "1px solid var(--cream-border)", padding: "0 var(--pad)",
          }}>
            <div style={{ maxWidth: "var(--max-w)", margin: "0 auto", height: 56, display: "flex", alignItems: "center", justifyContent: "space-between" }}>
              <button onClick={() => setActiveArticle(null)} style={{
                background: "none", border: "none", cursor: "pointer", color: "var(--navy-700)",
                fontFamily: "'Source Sans 3'", fontSize: 14, fontWeight: 600, gap: 6, padding: "8px 0",
              }}><ArrowLeft size={16} /> Back</button>
              <span style={{ fontFamily: "'JetBrains Mono'", fontSize: 10, color: "var(--ink-muted)", letterSpacing: "0.08em", textTransform: "uppercase" }}>{activeArticle.readTime}</span>
            </div>
          </nav>
          <article style={{ maxWidth: "var(--max-w)", margin: "0 auto", padding: "32px var(--pad) 80px", animation: "fadeUp 0.4s ease-out" }}>
            <div style={{ fontFamily: "'JetBrains Mono'", fontSize: 11, color: "var(--gold-500)", letterSpacing: "0.1em", textTransform: "uppercase", marginBottom: 12, fontWeight: 500 }}>{activeArticle.category} · {activeArticle.date}</div>
            <h1 style={{ fontFamily: "'Lora', Georgia, serif", fontSize: "clamp(26px, 5vw, 40px)", fontWeight: 700, lineHeight: 1.2, color: "var(--ink)", marginBottom: 16, letterSpacing: "-0.01em" }}>{activeArticle.title}</h1>
            <div style={{ display: "flex", alignItems: "center", gap: 12, marginBottom: 32, paddingBottom: 24, borderBottom: "1px solid var(--cream-border)" }}>
              <div style={{ width: 36, height: 36, borderRadius: "50%", background: "linear-gradient(135deg, var(--navy-700), var(--navy-900))", display: "flex", alignItems: "center", justifyContent: "center", fontFamily: "'Lora'", fontWeight: 700, fontSize: 14, color: "var(--gold-400)" }}>CC</div>
              <div>
                <div style={{ fontWeight: 600, fontSize: 14, color: "var(--ink)" }}>{activeArticle.author}</div>
                <div style={{ fontSize: 12, color: "var(--ink-muted)" }}>Army Veteran · 68W · AI Engineer</div>
              </div>
            </div>
            <div style={{ fontFamily: "'Source Sans 3'", fontSize: 17, lineHeight: 1.8, color: "var(--ink-light)" }}>
              {activeArticle.body.split("\n\n").map((para, i) => {
                if (para.startsWith("•")) {
                  return (<ul key={i} style={{ margin: "20px 0", paddingLeft: 20 }}>{para.split("\n").filter(l => l.trim()).map((li, j) => (<li key={j} style={{ marginBottom: 8, lineHeight: 1.6 }}>{li.replace(/^• /, "")}</li>))}</ul>);
                }
                return <p key={i} style={{ marginBottom: 20 }}>{para}</p>;
              })}
            </div>
            <div style={{ marginTop: 40, paddingTop: 24, borderTop: "1px solid var(--cream-border)", display: "flex", gap: 8, flexWrap: "wrap" }}>
              {activeArticle.tags.map(t => (
                <span key={t} style={{ padding: "6px 14px", borderRadius: 20, background: "var(--cream-warm)", border: "1px solid var(--cream-border)", fontFamily: "'JetBrains Mono'", fontSize: 11, color: "var(--ink-light)" }}>{t}</span>
              ))}
            </div>
            <div style={{ marginTop: 48 }}>
              <h3 style={{ fontFamily: "'Lora'", fontSize: 20, fontWeight: 700, color: "var(--ink)", marginBottom: 16 }}>Keep Reading</h3>
              {NEWS_POSTS.filter(p => p.id !== activeArticle.id).slice(0, 3).map(p => (
                <div key={p.id} onClick={() => openArticle(p)} style={{ padding: "16px 0", borderBottom: "1px solid var(--cream-border)", cursor: "pointer", display: "flex", justifyContent: "space-between", alignItems: "start", gap: 16 }}>
                  <div>
                    <div style={{ fontFamily: "'JetBrains Mono'", fontSize: 10, color: "var(--gold-500)", letterSpacing: "0.08em", textTransform: "uppercase", marginBottom: 4 }}>{p.category}</div>
                    <div style={{ fontFamily: "'Lora'", fontSize: 15, fontWeight: 600, color: "var(--ink)", lineHeight: 1.35 }}>{p.title}</div>
                  </div>
                  <span style={{ fontFamily: "'JetBrains Mono'", fontSize: 10, color: "var(--ink-muted)", whiteSpace: "nowrap", marginTop: 2 }}>{p.readTime}</span>
                </div>
              ))}
            </div>
          </article>
        </div>
      </>
    );
  }

  // ── Main Site ───────────────────────────────────────────────────
  return (
    <>
      <style>{globalCSS}</style>
      <div style={{ minHeight: "100vh", background: "var(--cream)" }}>

        {/* NAV */}
        <nav style={{ position: "sticky", top: 0, zIndex: 100, background: "rgba(11,26,46,0.97)", backdropFilter: "blur(12px)", borderBottom: "2px solid var(--gold-500)" }}>
          <div style={{ maxWidth: 1080, margin: "0 auto", padding: "0 var(--pad)", display: "flex", alignItems: "center", justifyContent: "space-between", height: 56 }}>
            <div style={{ display: "flex", alignItems: "center", gap: 10, cursor: "pointer" }} onClick={() => { setActiveArticle(null); setSelectedTag(null); window.scrollTo({ top: 0 }); }}>
              <div style={{ width: 30, height: 30, borderRadius: 6, background: "linear-gradient(135deg, var(--gold-500), var(--gold-300))", display: "flex", alignItems: "center", justifyContent: "center", fontFamily: "'Lora'", fontWeight: 700, fontSize: 14, color: "var(--navy-900)" }}>V2</div>
              <div style={{ lineHeight: 1.1 }}>
                <div style={{ fontFamily: "'Lora'", fontWeight: 700, fontSize: 14, color: "var(--white)" }}>Veteran 2 Veteran</div>
                <div style={{ fontFamily: "'JetBrains Mono'", fontSize: 8.5, color: "var(--gold-400)", letterSpacing: "0.12em", textTransform: "uppercase" }}>Claims Intelligence</div>
              </div>
            </div>
            <div style={{ display: "flex", gap: 24, alignItems: "center" }} className="dt-nav">
              {["News", "Guides", "Resources", "AI Tools", "About"].map(s => (
                <a key={s} href={`#${s.toLowerCase().replace(" ", "-")}`} style={{ fontFamily: "'Source Sans 3'", fontSize: 14, fontWeight: 500, color: "rgba(255,255,255,0.7)", textDecoration: "none", cursor: "pointer", minHeight: 44, padding: "0 2px", transition: "color 0.2s" }}
                  onMouseEnter={e => e.target.style.color = "var(--gold-400)"} onMouseLeave={e => e.target.style.color = "rgba(255,255,255,0.7)"}>{s}</a>
              ))}
            </div>
            <button onClick={() => setMobileMenu(!mobileMenu)} className="mob-toggle" style={{ background: "none", border: "none", color: "var(--white)", cursor: "pointer", padding: 8, display: "none", minHeight: 44, justifyContent: "center" }}>
              {mobileMenu ? <CloseIcon /> : <MenuIcon />}
            </button>
          </div>
          {mobileMenu && (
            <div style={{ padding: "8px var(--pad) 16px", background: "var(--navy-800)", animation: "fadeIn 0.2s ease-out" }}>
              {["News", "Guides", "Resources", "AI Tools", "About"].map(s => (
                <a key={s} href={`#${s.toLowerCase().replace(" ", "-")}`} onClick={() => setMobileMenu(false)}
                  style={{ display: "flex", padding: "14px 0", borderBottom: "1px solid rgba(255,255,255,0.06)", color: "rgba(255,255,255,0.8)", fontFamily: "'Source Sans 3'", fontSize: 16, textDecoration: "none", minHeight: 44, alignItems: "center" }}>{s}</a>
              ))}
            </div>
          )}
          <style>{`@media (max-width: 768px) { .dt-nav { display: none !important; } .mob-toggle { display: flex !important; } }`}</style>
        </nav>

        {/* HERO — compact, content-forward */}
        <section style={{ background: "var(--navy-900)", padding: "40px var(--pad) 48px", position: "relative", overflow: "hidden" }}>
          <div style={{ position: "absolute", inset: 0, pointerEvents: "none", background: "radial-gradient(ellipse at 30% 0%, rgba(200,162,50,0.08), transparent 60%)" }} />
          <div style={{ maxWidth: 1080, margin: "0 auto", position: "relative", zIndex: 1 }}>
            <p style={{ fontFamily: "'JetBrains Mono'", fontSize: 11, color: "var(--gold-400)", letterSpacing: "0.14em", textTransform: "uppercase", marginBottom: 12 }}>VA Claims News & Strategy</p>
            <h1 style={{ fontFamily: "'Lora', Georgia, serif", fontSize: "clamp(28px, 5.5vw, 48px)", fontWeight: 700, color: "var(--white)", lineHeight: 1.15, marginBottom: 14, letterSpacing: "-0.01em", maxWidth: 560 }}>
              Know your rights.<br/>Win your claim.
            </h1>
            <p style={{ fontFamily: "'Source Sans 3'", fontSize: "clamp(15px, 2vw, 18px)", color: "rgba(255,255,255,0.6)", lineHeight: 1.55, maxWidth: 500, marginBottom: 24 }}>
              Plain-language news, CAVC analysis, and claims strategy — from a veteran who's been in the trenches.
            </p>
            <div style={{ display: "flex", gap: 12, flexWrap: "wrap" }}>
              <a href="#news" style={{ background: "var(--gold-500)", border: "none", padding: "12px 24px", borderRadius: 8, fontWeight: 600, fontSize: 14, color: "var(--navy-900)", cursor: "pointer", textDecoration: "none", gap: 6, fontFamily: "'Source Sans 3'", justifyContent: "center" }}>
                Read Latest <ArrowRight />
              </a>
              <button onClick={() => setShowChat(true)} style={{ background: "rgba(255,255,255,0.08)", border: "1px solid rgba(255,255,255,0.2)", padding: "12px 24px", borderRadius: 8, fontWeight: 600, fontSize: 14, color: "var(--white)", cursor: "pointer", gap: 6, fontFamily: "'Source Sans 3'", justifyContent: "center" }}>
                <BookIcon /> Ask AI
              </button>
            </div>
          </div>
        </section>

        {/* NEWS FEED */}
        <section id="news" style={{ padding: "40px var(--pad)", maxWidth: 1080, margin: "0 auto" }}>
          <h2 style={{ fontFamily: "'Lora'", fontSize: 22, fontWeight: 700, color: "var(--ink)", marginBottom: 20 }}>Latest Posts</h2>

          <div className="hide-scroll" style={{ display: "flex", gap: 8, overflowX: "auto", paddingBottom: 16, marginBottom: 8 }}>
            <button onClick={() => setSelectedTag(null)} style={{ padding: "8px 16px", borderRadius: 20, whiteSpace: "nowrap", border: "1px solid", fontSize: 13, fontWeight: 500, cursor: "pointer", fontFamily: "'Source Sans 3'", minHeight: 36, background: !selectedTag ? "var(--ink)" : "transparent", color: !selectedTag ? "var(--white)" : "var(--ink-light)", borderColor: !selectedTag ? "var(--ink)" : "var(--cream-border)", justifyContent: "center" }}>All</button>
            {allTags.map(t => (
              <button key={t} onClick={() => setSelectedTag(selectedTag === t ? null : t)} style={{ padding: "8px 16px", borderRadius: 20, whiteSpace: "nowrap", border: "1px solid", fontSize: 13, fontWeight: 500, cursor: "pointer", fontFamily: "'Source Sans 3'", minHeight: 36, background: selectedTag === t ? "var(--ink)" : "transparent", color: selectedTag === t ? "var(--white)" : "var(--ink-light)", borderColor: selectedTag === t ? "var(--ink)" : "var(--cream-border)", justifyContent: "center" }}>{t}</button>
            ))}
          </div>

          {/* Featured */}
          {!selectedTag && (
            <div onClick={() => openArticle(NEWS_POSTS[0])} style={{ background: "var(--navy-900)", borderRadius: "var(--radius)", overflow: "hidden", marginBottom: 20, cursor: "pointer", transition: "box-shadow 0.3s", position: "relative" }}
              onMouseEnter={e => e.currentTarget.style.boxShadow = "0 8px 24px rgba(11,26,46,0.25)"} onMouseLeave={e => e.currentTarget.style.boxShadow = "none"}>
              <div style={{ padding: "28px 24px" }}>
                <div style={{ display: "inline-flex", padding: "3px 10px", borderRadius: 4, background: "rgba(200,162,50,0.15)", border: "1px solid rgba(200,162,50,0.3)", fontFamily: "'JetBrains Mono'", fontSize: 10, fontWeight: 600, color: "var(--gold-400)", letterSpacing: "0.08em", textTransform: "uppercase", marginBottom: 14, minHeight: "auto" }}>Featured</div>
                <div style={{ fontFamily: "'JetBrains Mono'", fontSize: 10, color: "var(--gold-400)", letterSpacing: "0.08em", textTransform: "uppercase", marginBottom: 10 }}>{NEWS_POSTS[0].category} · {NEWS_POSTS[0].date}</div>
                <h3 style={{ fontFamily: "'Lora'", fontSize: "clamp(20px, 4vw, 28px)", fontWeight: 700, color: "var(--white)", lineHeight: 1.25, marginBottom: 10 }}>{NEWS_POSTS[0].title}</h3>
                <p style={{ fontFamily: "'Source Sans 3'", fontSize: 15, color: "rgba(255,255,255,0.6)", lineHeight: 1.55, marginBottom: 16 }}>{NEWS_POSTS[0].excerpt}</p>
                <div style={{ display: "flex", alignItems: "center", gap: 8, fontFamily: "'Source Sans 3'", fontSize: 14, fontWeight: 600, color: "var(--gold-400)", minHeight: "auto" }}>
                  Read full article <ArrowRight />
                </div>
              </div>
            </div>
          )}

          {/* Post list */}
          <div style={{ display: "flex", flexDirection: "column", gap: 2 }}>
            {filtered.filter(p => selectedTag || !p.featured).map((post, i) => (
              <article key={post.id} onClick={() => openArticle(post)} style={{ padding: "20px 0", borderBottom: "1px solid var(--cream-border)", cursor: "pointer", animation: `fadeUp 0.3s ease-out ${i * 0.05}s both` }}>
                <div style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 6 }}>
                  <span style={{ fontFamily: "'JetBrains Mono'", fontSize: 10, fontWeight: 500, color: "var(--gold-500)", letterSpacing: "0.08em", textTransform: "uppercase" }}>{post.category}</span>
                  <span style={{ color: "var(--cream-border)" }}>·</span>
                  <span style={{ fontFamily: "'JetBrains Mono'", fontSize: 10, color: "var(--ink-muted)" }}>{post.date}</span>
                </div>
                <h3 style={{ fontFamily: "'Lora'", fontSize: "clamp(16px, 3vw, 19px)", fontWeight: 600, color: "var(--ink)", lineHeight: 1.35, marginBottom: 6 }}>{post.title}</h3>
                <p style={{ fontFamily: "'Source Sans 3'", fontSize: 14, color: "var(--ink-light)", lineHeight: 1.5, display: "-webkit-box", WebkitLineClamp: 2, WebkitBoxOrient: "vertical", overflow: "hidden" }}>{post.excerpt}</p>
                <div style={{ display: "flex", alignItems: "center", gap: 6, marginTop: 8, fontSize: 12, color: "var(--ink-muted)", fontFamily: "'Source Sans 3'", minHeight: "auto" }}>
                  <ClockIcon /> {post.readTime}
                  <div style={{ display: "flex", gap: 4, marginLeft: "auto" }}>
                    {post.tags.slice(0, 2).map(t => (
                      <span key={t} style={{ padding: "2px 8px", borderRadius: 4, background: "var(--cream-warm)", fontSize: 10, fontFamily: "'JetBrains Mono'", color: "var(--ink-muted)" }}>{t}</span>
                    ))}
                  </div>
                </div>
              </article>
            ))}
          </div>
        </section>

        {/* QUICK GUIDES */}
        <section id="guides" style={{ padding: "48px var(--pad)", background: "var(--white)", borderTop: "1px solid var(--cream-border)", borderBottom: "1px solid var(--cream-border)" }}>
          <div style={{ maxWidth: 1080, margin: "0 auto" }}>
            <h2 style={{ fontFamily: "'Lora'", fontSize: 22, fontWeight: 700, color: "var(--ink)", marginBottom: 6 }}>Quick Guides</h2>
            <p style={{ fontFamily: "'Source Sans 3'", fontSize: 15, color: "var(--ink-muted)", marginBottom: 24 }}>Plain-English explanations of what every veteran needs to know.</p>
            <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(260px, 1fr))", gap: 12 }}>
              {QUICK_GUIDES.map((g, i) => (
                <div key={i} style={{ display: "flex", alignItems: "center", gap: 14, padding: "16px 18px", borderRadius: "var(--radius)", border: "1px solid var(--cream-border)", background: "var(--cream)", cursor: "pointer", transition: "border-color 0.2s, background 0.2s", minHeight: 44 }}
                  onMouseEnter={e => { e.currentTarget.style.borderColor = "var(--gold-500)"; e.currentTarget.style.background = "var(--cream-warm)"; }}
                  onMouseLeave={e => { e.currentTarget.style.borderColor = "var(--cream-border)"; e.currentTarget.style.background = "var(--cream)"; }}>
                  <span style={{ fontSize: 22, flexShrink: 0, lineHeight: 1 }}>{g.icon}</span>
                  <div>
                    <div style={{ fontWeight: 600, fontSize: 14, color: "var(--ink)", lineHeight: 1.2 }}>{g.title}</div>
                    <div style={{ fontSize: 13, color: "var(--ink-muted)", lineHeight: 1.35, marginTop: 2 }}>{g.desc}</div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* RESOURCES */}
        <section id="resources" style={{ padding: "48px var(--pad)", maxWidth: 1080, margin: "0 auto" }}>
          <h2 style={{ fontFamily: "'Lora'", fontSize: 22, fontWeight: 700, color: "var(--ink)", marginBottom: 6 }}>Resources & Tools</h2>
          <p style={{ fontFamily: "'Source Sans 3'", fontSize: 15, color: "var(--ink-muted)", marginBottom: 24 }}>Useful references for navigating the VA system.</p>
          <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(280px, 1fr))", gap: 14 }}>
            {[
              { icon: "📋", title: "Claims Process Guide", desc: "From initial filing to Board appeal — the complete walkthrough." },
              { icon: "⚖️", title: "CAVC Precedent Library", desc: "Plain-language summaries of key Court decisions." },
              { icon: "📖", title: "38 CFR Quick Ref", desc: "Find the regulation sections for your claim type." },
              { icon: "🏥", title: "C&P Exam Prep", desc: "What to expect, bring, and how to get an accurate exam." },
              { icon: "📊", title: "Rating Calculator", desc: "Estimate your combined rating using VA math." },
              { icon: "🔍", title: "BVA Decision Search", desc: "Search Board decisions by keyword, issue, and outcome." },
            ].map((r, i) => (
              <div key={i} style={{ padding: "20px", borderRadius: "var(--radius)", border: "1px solid var(--cream-border)", background: "var(--white)", cursor: "pointer", transition: "all 0.2s", display: "flex", gap: 14 }}
                onMouseEnter={e => { e.currentTarget.style.borderColor = "var(--gold-500)"; e.currentTarget.style.transform = "translateY(-2px)"; }}
                onMouseLeave={e => { e.currentTarget.style.borderColor = "var(--cream-border)"; e.currentTarget.style.transform = "translateY(0)"; }}>
                <div style={{ width: 40, height: 40, borderRadius: 8, background: "var(--navy-900)", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 20, flexShrink: 0 }}>{r.icon}</div>
                <div>
                  <div style={{ fontWeight: 600, fontSize: 15, color: "var(--ink)", marginBottom: 3 }}>{r.title}</div>
                  <div style={{ fontSize: 13, color: "var(--ink-light)", lineHeight: 1.45 }}>{r.desc}</div>
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* AI TOOLS — secondary */}
        <section id="ai-tools" style={{ padding: "48px var(--pad)", background: "var(--navy-900)", color: "var(--white)" }}>
          <div style={{ maxWidth: 1080, margin: "0 auto" }}>
            <div style={{ fontFamily: "'JetBrains Mono'", fontSize: 10, color: "var(--gold-400)", letterSpacing: "0.12em", textTransform: "uppercase", marginBottom: 8 }}>AI-Powered Research</div>
            <h2 style={{ fontFamily: "'Lora'", fontSize: 22, fontWeight: 700, marginBottom: 6 }}>Research Tools</h2>
            <p style={{ fontSize: 15, color: "rgba(255,255,255,0.6)", marginBottom: 24, maxWidth: 500 }}>Professional-grade AI for searching BVA decisions, CAVC precedent, and VA regulations.</p>
            <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
              {AI_TOOLS.map((tool, i) => (
                <div key={i} onClick={() => setExpandedTool(expandedTool === i ? null : i)} style={{ padding: "16px 20px", borderRadius: "var(--radius)", border: "1px solid", borderColor: expandedTool === i ? "var(--gold-500)" : "rgba(255,255,255,0.1)", background: expandedTool === i ? "rgba(255,255,255,0.05)" : "transparent", cursor: "pointer", transition: "all 0.2s" }}>
                  <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                    <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
                      <span style={{ fontWeight: 600, fontSize: 15 }}>{tool.name}</span>
                      <span style={{ padding: "2px 8px", borderRadius: 4, fontSize: 10, fontFamily: "'JetBrains Mono'", fontWeight: 600, letterSpacing: "0.06em", textTransform: "uppercase", background: tool.status === "Live" ? "rgba(34,197,94,0.15)" : "rgba(234,179,8,0.15)", color: tool.status === "Live" ? "#22c55e" : "#eab308", border: `1px solid ${tool.status === "Live" ? "rgba(34,197,94,0.3)" : "rgba(234,179,8,0.3)"}`, display: "inline-flex", alignItems: "center", gap: 4, minHeight: "auto" }}>
                        {tool.status === "Live" && <span style={{ width: 5, height: 5, borderRadius: "50%", background: "#22c55e" }} />}{tool.status}
                      </span>
                    </div>
                    <div style={{ transform: expandedTool === i ? "rotate(180deg)" : "rotate(0)", transition: "transform 0.2s", color: "var(--ink-muted)" }}><ChevronDown /></div>
                  </div>
                  {expandedTool === i && (<p style={{ fontSize: 14, color: "rgba(255,255,255,0.6)", lineHeight: 1.5, marginTop: 10, animation: "fadeIn 0.2s ease-out" }}>{tool.desc}</p>)}
                </div>
              ))}
            </div>
            <button onClick={() => setShowChat(true)} style={{ marginTop: 24, background: "var(--gold-500)", border: "none", padding: "14px 28px", borderRadius: 8, fontWeight: 700, fontSize: 15, color: "var(--navy-900)", cursor: "pointer", fontFamily: "'Source Sans 3'", gap: 8, justifyContent: "center", width: "100%" }}>
              Try the Research Assistant <ArrowRight />
            </button>
          </div>
        </section>

        {/* ABOUT */}
        <section id="about" style={{ padding: "48px var(--pad)", maxWidth: 1080, margin: "0 auto" }}>
          <div style={{ display: "grid", gridTemplateColumns: "1fr", gap: 32 }} className="about-grid">
            <div>
              <div style={{ fontFamily: "'JetBrains Mono'", fontSize: 10, color: "var(--gold-500)", letterSpacing: "0.12em", textTransform: "uppercase", marginBottom: 10 }}>About</div>
              <h2 style={{ fontFamily: "'Lora'", fontSize: "clamp(24px, 4vw, 32px)", fontWeight: 700, color: "var(--ink)", lineHeight: 1.2, marginBottom: 16 }}>Built by a Veteran, for Veterans</h2>
              <p style={{ fontSize: 16, color: "var(--ink-light)", lineHeight: 1.7, marginBottom: 14 }}>Veteran 2 Veteran was founded by Chris Combs — a U.S. Army veteran, former combat medic (68W), and AI software engineer with over 15 years of VA claims experience.</p>
              <p style={{ fontSize: 16, color: "var(--ink-light)", lineHeight: 1.7, marginBottom: 20 }}>After years watching veterans struggle to navigate the VA system, Chris combined deep domain expertise in veterans law with modern AI to build tools that level the playing field.</p>
              <div style={{ display: "flex", gap: 10, flexWrap: "wrap" }}>
                {[{ label: "Army Veteran", icon: "🎖️" }, { label: "68W Medic", icon: "⚕️" }, { label: "AI Engineer", icon: "🤖" }, { label: "15+ yrs VA", icon: "📋" }].map((b, i) => (
                  <div key={i} style={{ display: "flex", alignItems: "center", gap: 6, padding: "6px 14px", borderRadius: 6, background: "var(--cream-warm)", border: "1px solid var(--cream-border)", minHeight: "auto" }}>
                    <span style={{ fontSize: 14 }}>{b.icon}</span>
                    <span style={{ fontFamily: "'JetBrains Mono'", fontSize: 11, color: "var(--ink-light)" }}>{b.label}</span>
                  </div>
                ))}
              </div>
            </div>
            <div style={{ background: "var(--navy-900)", borderRadius: "var(--radius)", padding: "28px 24px", position: "relative", overflow: "hidden" }}>
              <div style={{ position: "absolute", top: -30, right: -30, width: 100, height: 100, borderRadius: "50%", background: "rgba(200,162,50,0.08)" }} />
              <div style={{ fontFamily: "'Lora'", fontSize: 18, fontWeight: 700, color: "var(--white)", marginBottom: 12, position: "relative" }}>Our Mission</div>
              <p style={{ fontSize: 15, color: "rgba(255,255,255,0.65)", lineHeight: 1.65, position: "relative" }}>To ensure every veteran has access to the same quality of research and analysis that was once only available to large law firms — powered by AI, grounded in years of real VA experience.</p>
              <div style={{ marginTop: 20, paddingTop: 16, borderTop: "1px solid rgba(255,255,255,0.08)", display: "flex", gap: 8, flexWrap: "wrap" }}>
                {["Veterans", "VSOs", "Attorneys", "Claims Agents"].map(s => (
                  <span key={s} style={{ padding: "5px 12px", borderRadius: 6, border: "1px solid rgba(255,255,255,0.12)", fontSize: 13, color: "rgba(255,255,255,0.6)", minHeight: "auto", display: "inline-flex", alignItems: "center" }}>{s}</span>
                ))}
              </div>
            </div>
          </div>
          <style>{`@media (min-width: 768px) { .about-grid { grid-template-columns: 1.2fr 1fr !important; align-items: start; } }`}</style>
        </section>

        {/* FOOTER */}
        <footer style={{ background: "var(--navy-900)", padding: "40px var(--pad) 28px", borderTop: "2px solid var(--gold-500)" }}>
          <div style={{ maxWidth: 1080, margin: "0 auto", display: "grid", gridTemplateColumns: "1fr", gap: 32 }} className="footer-grid">
            <div>
              <div style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 12 }}>
                <div style={{ width: 26, height: 26, borderRadius: 5, background: "linear-gradient(135deg, var(--gold-500), var(--gold-300))", display: "flex", alignItems: "center", justifyContent: "center", fontFamily: "'Lora'", fontWeight: 700, fontSize: 12, color: "var(--navy-900)" }}>V2</div>
                <span style={{ fontFamily: "'Lora'", fontSize: 14, fontWeight: 700, color: "var(--white)" }}>Veteran 2 Veteran LLC</span>
              </div>
              <p style={{ fontSize: 13, color: "rgba(255,255,255,0.4)", lineHeight: 1.5, maxWidth: 300 }}>AI-powered claims intelligence for veterans and the professionals who serve them. Based in Ohio.</p>
            </div>
            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr 1fr", gap: 24 }}>
              {[{ t: "Content", l: ["News", "Guides", "Resources", "Blog Archive"] }, { t: "Tools", l: ["BVA Search", "CAVC Analyzer", "CFR Navigator", "AI Assistant"] }, { t: "Company", l: ["About", "Contact", "Privacy", "Terms"] }].map((c, i) => (
                <div key={i}>
                  <div style={{ fontFamily: "'JetBrains Mono'", fontSize: 9, color: "var(--gold-400)", letterSpacing: "0.14em", textTransform: "uppercase", marginBottom: 12 }}>{c.t}</div>
                  {c.l.map(l => (<div key={l} style={{ fontSize: 13, color: "rgba(255,255,255,0.45)", marginBottom: 8, cursor: "pointer" }}>{l}</div>))}
                </div>
              ))}
            </div>
          </div>
          <div style={{ maxWidth: 1080, margin: "24px auto 0", paddingTop: 20, borderTop: "1px solid rgba(255,255,255,0.06)", fontSize: 11, color: "rgba(255,255,255,0.25)", fontFamily: "'JetBrains Mono'", display: "flex", justifyContent: "space-between", flexWrap: "wrap", gap: 8 }}>
            <span>© 2026 Veteran 2 Veteran LLC</span>
            <span>Not legal advice. Not affiliated with VA.</span>
          </div>
          <style>{`@media (min-width: 768px) { .footer-grid { grid-template-columns: 1fr 2fr !important; } }`}</style>
        </footer>

        {/* FLOATING CHAT PANEL */}
        {showChat && (
          <div style={{ position: "fixed", inset: 0, zIndex: 200, background: "rgba(0,0,0,0.4)", animation: "fadeIn 0.2s ease-out" }} onClick={(e) => { if (e.target === e.currentTarget) setShowChat(false); }}>
            <div style={{ position: "absolute", bottom: 0, left: 0, right: 0, maxHeight: "85vh", height: 520, background: "var(--white)", borderRadius: "16px 16px 0 0", display: "flex", flexDirection: "column", animation: "slideUp 0.3s ease-out", boxShadow: "0 -8px 32px rgba(0,0,0,0.2)" }} className="chat-panel">
              <div style={{ padding: "14px 20px", background: "var(--navy-900)", borderRadius: "16px 16px 0 0", display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
                  <div style={{ width: 7, height: 7, borderRadius: "50%", background: "#22c55e", animation: "dotPulse 2s infinite" }} />
                  <span style={{ fontFamily: "'JetBrains Mono'", fontSize: 12, color: "rgba(255,255,255,0.8)" }}>V2V Research Assistant</span>
                </div>
                <button onClick={() => setShowChat(false)} style={{ background: "none", border: "none", color: "rgba(255,255,255,0.6)", cursor: "pointer", padding: 4, minHeight: 44, justifyContent: "center" }}><CloseIcon /></button>
              </div>
              <div style={{ flex: 1, overflowY: "auto", padding: "16px", display: "flex", flexDirection: "column", gap: 12 }}>
                {chatMsgs.map((m, i) => (
                  <div key={i} style={{ display: "flex", justifyContent: m.role === "user" ? "flex-end" : "flex-start" }}>
                    <div style={{ maxWidth: "88%", padding: "10px 14px", borderRadius: m.role === "user" ? "12px 12px 2px 12px" : "12px 12px 12px 2px", background: m.role === "user" ? "var(--navy-800)" : "var(--cream)", color: m.role === "user" ? "var(--white)" : "var(--ink)", fontSize: 14, lineHeight: 1.55, border: m.role === "ai" ? "1px solid var(--cream-border)" : "none" }}
                      dangerouslySetInnerHTML={{ __html: m.text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>').replace(/\n/g, '<br/>') }} />
                  </div>
                ))}
                {typing && (
                  <div style={{ display: "flex", gap: 4, padding: "10px 14px", background: "var(--cream)", borderRadius: "12px 12px 12px 2px", width: "fit-content", border: "1px solid var(--cream-border)" }}>
                    {[0,1,2].map(i => (<div key={i} style={{ width: 5, height: 5, borderRadius: "50%", background: "var(--navy-700)", animation: `dotPulse 1.2s infinite ${i * 0.2}s` }} />))}
                  </div>
                )}
                <div ref={chatEnd} />
              </div>
              <div className="hide-scroll" style={{ padding: "6px 12px", display: "flex", gap: 6, overflowX: "auto", borderTop: "1px solid var(--cream-border)" }}>
                {["TDIU eligibility", "Search BVA decisions", "38 CFR lookup", "Secondary conditions"].map(q => (
                  <button key={q} onClick={() => setChatInput(q)} style={{ padding: "6px 12px", borderRadius: 6, whiteSpace: "nowrap", border: "1px solid var(--cream-border)", background: "transparent", fontFamily: "'JetBrains Mono'", fontSize: 10, color: "var(--ink-light)", cursor: "pointer", minHeight: 32, justifyContent: "center" }}>{q}</button>
                ))}
              </div>
              <div style={{ padding: "10px 12px", display: "flex", gap: 8, borderTop: "1px solid var(--cream-border)", paddingBottom: "max(10px, env(safe-area-inset-bottom))" }}>
                <input value={chatInput} onChange={e => setChatInput(e.target.value)} onKeyDown={e => e.key === "Enter" && handleChat()} placeholder="Ask about your claim..."
                  style={{ flex: 1, padding: "10px 14px", borderRadius: 8, border: "1px solid var(--cream-border)", fontSize: 15, fontFamily: "'Source Sans 3'", outline: "none", background: "var(--cream)", WebkitAppearance: "none" }}
                  onFocus={e => e.target.style.borderColor = "var(--gold-500)"} onBlur={e => e.target.style.borderColor = "var(--cream-border)"} />
                <button onClick={handleChat} style={{ width: 44, height: 44, borderRadius: 8, border: "none", background: chatInput.trim() ? "var(--navy-900)" : "var(--cream-border)", color: chatInput.trim() ? "var(--gold-400)" : "var(--ink-muted)", cursor: chatInput.trim() ? "pointer" : "default", justifyContent: "center", flexShrink: 0 }}><SendIcon /></button>
              </div>
            </div>
            <style>{`@media (min-width: 768px) { .chat-panel { max-width: 480px !important; right: 24px !important; left: auto !important; } }`}</style>
          </div>
        )}

        {/* FAB */}
        {!showChat && (
          <button onClick={() => setShowChat(true)} style={{ position: "fixed", bottom: 20, right: 20, zIndex: 90, width: 56, height: 56, borderRadius: 28, background: "var(--navy-900)", border: "2px solid var(--gold-500)", boxShadow: "0 4px 20px rgba(11,26,46,0.3)", cursor: "pointer", justifyContent: "center", color: "var(--gold-400)", fontSize: 22 }}>
            <BookIcon />
          </button>
        )}
      </div>
    </>
  );
}
