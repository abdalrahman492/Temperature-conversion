<!doctype html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>آلة حاسبة بسيطة</title>
  <style>
    :root{
      --bg:#0f172a;          /* slate-900 */
      --panel:#111827;       /* gray-900 */
      --muted:#94a3b8;       /* slate-400 */
      --card:#0b1224;        /* deep card */
      --acc:#22d3ee;         /* cyan-400 */
      --acc-2:#60a5fa;       /* blue-400 */
      --text:#e5e7eb;        /* gray-200 */
      --danger:#f87171;      /* red-400 */
      --ok:#34d399;          /* green-400 */
      --shadow: 0 10px 25px rgba(0,0,0,.35), inset 0 0 0 1px rgba(255,255,255,.03);
      --radius: 18px;
    }
    *{box-sizing:border-box}
    body{
      margin:0;
      min-height:100dvh;
      background: radial-gradient(1200px 600px at 20% -10%, rgba(34,211,238,.18), transparent 60%),
                  radial-gradient(1000px 500px at 110% 10%, rgba(96,165,250,.16), transparent 60%),
                  var(--bg);
      color:var(--text);
      font-family: system-ui, -apple-system, Segoe UI, Roboto, "Noto Naskh Arabic", Tahoma, Arial, sans-serif;
      display:grid; place-items:center; padding:24px;
    }

    .wrap{width: min(720px, 96vw);}

    .card{
      background: linear-gradient(180deg, rgba(255,255,255,.03), rgba(255,255,255,.01)), var(--card);
      border: 1px solid rgba(255,255,255,.06);
      box-shadow: var(--shadow);
      border-radius: var(--radius);
      padding: clamp(16px, 3vw, 28px);
    }

    h1{
      margin:0 0 8px; font-weight:800; letter-spacing:.3px;
      background: linear-gradient(90deg, var(--acc), var(--acc-2));
      -webkit-background-clip: text; background-clip: text; color: transparent;
      font-size: clamp(20px, 3.5vw, 30px);
    }
    .sub{color:var(--muted); margin:0 0 18px; font-size: 14px}

    .grid{display:grid; gap:12px; grid-template-columns: 1fr auto 1fr; align-items:end}
    .field{display:flex; flex-direction:column; gap:6px}
    label{font-size:12px; color:var(--muted)}
    input, select{
      background: #0b1328;
      color:var(--text);
      border:1px solid rgba(255,255,255,.08);
      border-radius: 12px;
      padding:12px 14px;
      outline:none;
      transition: .2s border-color, .2s box-shadow;
    }
    input:focus, select:focus{ border-color: var(--acc); box-shadow: 0 0 0 4px rgba(34,211,238,.12)}

    .op{ display:flex; flex-direction:column; gap:6px; align-items:center}
    .op select{min-width:92px; text-align:center}

    .actions{ display:flex; gap:10px; margin-top:14px; flex-wrap:wrap}
    .btn{
      cursor:pointer; user-select:none;
      padding:12px 16px; border-radius:12px; font-weight:700; letter-spacing:.2px;
      background: linear-gradient(180deg, rgba(34,211,238,.25), rgba(34,211,238,.18));
      border:1px solid rgba(34,211,238,.35);
      color:#032b33;
      transition: .2s transform, .2s filter;
    }
    .btn:hover{ filter:brightness(1.05)}
    .btn:active{ transform: translateY(1px)}

    .ghost{ background:transparent; color:var(--text); border-color: rgba(255,255,255,.12)}

    .result{
      margin-top:18px; padding:14px; border-radius:12px;
      background:#0b1328; border:1px dashed rgba(255,255,255,.14);
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace;
      display:flex; align-items:center; gap:10px;
    }
    .badge{font-size:12px; padding:6px 10px; border-radius:999px; background:rgba(52,211,153,.12); color:var(--ok); border:1px solid rgba(52,211,153,.35)}
    .error{ background: rgba(248,113,113,.12); color: var(--danger); border-color: rgba(248,113,113,.4)}

    .history{ margin-top:20px }
    .history h2{ font-size:14px; color:var(--muted); margin:0 0 10px }
    .list{ display:grid; gap:8px }
    .item{
      padding:10px 12px; border:1px solid rgba(255,255,255,.06); border-radius:10px;
      background:#0b1328; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      display:flex; justify-content:space-between; align-items:center; gap:10px;
    }
    .item small{ color:var(--muted) }

    footer{ margin-top:18px; color:var(--muted); font-size:12px; text-align:center }

    @media (max-width:640px){
      .grid{ grid-template-columns: 1fr; }
      .op{ align-items:stretch }
      .op select{ min-width: auto }
    }
  </style>
</head>
<body>
  <main class="wrap">
    <section class="card" aria-label="آلة حاسبة">
      <h