---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Poppins:wght@400;500;600&family=Noto+Sans+SC:wght@400;500;600&display=swap');

/* ===== 平滑滚动 ===== */
html {
  scroll-behavior: smooth;
}

/* ===== 基础配色 & 字体 ===== */
:root {
  --cv-font-body: 'Poppins','Noto Sans SC',-apple-system,system-ui,sans-serif;
  --cv-font-heading: 'DM Serif Display','Noto Sans SC',serif;

  --cv-accent: #2563eb;              /* 主色：偏学术的蓝 */
  --cv-accent-warm: #f59e0b;         /* 点缀：和头像暖色呼应 */
  --cv-accent-soft: rgba(37,99,235,0.08);

  --cv-border: #e2e8f0;
  --cv-border-soft: #edf2f7;

  --cv-text-main: #0f172a;
  --cv-text-muted: #64748b;
}

/* ===== 页面整体容器 ===== */
.cv-page {
  max-width: 920px;
  margin: 0 auto;
  padding: 2.5rem 1.5rem 3rem;
}

.cv-main {
  font-family: var(--cv-font-body);
}

/* ===== 入场动画 ===== */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.cv-section {
  animation: fadeInUp 0.6s ease-out forwards;
}

.cv-section:nth-child(1) { animation-delay: 0.1s; }
.cv-section:nth-child(2) { animation-delay: 0.2s; }
.cv-section:nth-child(3) { animation-delay: 0.3s; }
.cv-section:nth-child(4) { animation-delay: 0.4s; }
.cv-section:nth-child(5) { animation-delay: 0.5s; }
.cv-section:nth-child(6) { animation-delay: 0.6s; }

/* ===== 通用 Section 卡片 ===== */
.cv-section {
  background: linear-gradient(145deg,#ffffff,#f9fafb);
  border-radius: 20px;
  border: 1px solid var(--cv-border);
  padding: 1.8rem 1.7rem 1.7rem;
  margin-bottom: 1.6rem;
  box-shadow: 0 14px 32px rgba(15,23,42,0.06);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  scroll-margin-top: 100px; /* 为 sticky header 预留空间 */
}

.cv-section:hover {
  transform: translateY(-4px);
  box-shadow: 0 20px 40px rgba(15,23,42,0.1);
}

body[data-theme="dark"] .cv-section {
  background: radial-gradient(circle at top,#020617,#020617);
  border-color: #1f2937;
}

/* ===== 顶层标题 ===== */
.cv-section .section-title {
  font-family: var(--cv-font-heading);
  font-size: 1.55rem;
  font-weight: 500;
  letter-spacing: 0.04em;
  margin: 0 0 1rem;
  color: var(--cv-text-main);
  display: flex;
  align-items: center;
}

body[data-theme="dark"] .cv-section .section-title {
  color: #e5e7eb;
}

.cv-section .section-title::before {
  content: "";
  width: 6px;
  height: 1em;
  border-radius: 999px;
  margin-right: 0.6rem;
  background: linear-gradient(180deg,var(--cv-accent),var(--cv-accent-warm));
  align-self: center;
}

.cv-section .section-title::after {
  content: "";
  flex: 1;
  height: 2px;
  border-radius: 999px;
  margin-left: 0.75rem;
  background: linear-gradient(to right, var(--cv-accent-soft), transparent);
}

/* ===== 二级标题（Journal Article / Competition Awards 等）===== */
.subsection-title {
  font-family: var(--cv-font-body);
  font-size: 1.02rem;
  font-weight: 600;
  margin: 0.4rem 0 0.6rem;
  color: var(--cv-text-main);
}

body[data-theme="dark"] .subsection-title {
  color: #e5e7eb;
}

/* ===== 基础正文排版 ===== */
.cv-section p,
.cv-section li {
  font-size: 0.96rem;
  line-height: 1.7;
  color: var(--cv-text-main);
}

body[data-theme="dark"] .cv-section p,
body[data-theme="dark"] .cv-section li {
  color: #e5e7eb;
}

.cv-section ul {
  margin-top: 0.2rem;
  padding-left: 1.2rem;
}

.cv-section li {
  position: relative;
  padding-left: 0.3rem;
}

.cv-section li::marker {
  color: var(--cv-accent);
  font-weight: bold;
}

.cv-section li + li {
  margin-top: 0.35rem;
}

/* 列表项悬停效果 */
.info-block li {
  padding: 0.25rem 0.4rem;
  border-radius: 6px;
  margin-left: -0.4rem;
  transition: background-color 0.2s ease;
}

.info-block li:hover {
  background-color: rgba(37, 99, 235, 0.04);
}

/* ===== Publication：简洁卡片样式 ===== */
.pub-category {
  margin-top: 0.4rem;
}

.pub-list {
  list-style: none;
  padding-left: 0;
  margin: 0.3rem 0 0;
  display: flex;
  flex-direction: column;
  gap: 0.55rem;
}

.pub-item {
  display: grid;
  grid-template-columns: auto minmax(0,1fr);
  column-gap: 0.8rem;
  align-items: flex-start;
  padding: 0.75rem 1rem;
  border-radius: 16px;
  border: 1px solid var(--cv-border-soft);
  background: radial-gradient(circle at top left,#eff6ff,#f9fafb);
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}

.pub-item:hover {
  transform: translateX(6px);
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.1);
  border-color: var(--cv-accent);
}

body[data-theme="dark"] .pub-item {
  border-color: #1f2937;
  background: radial-gradient(circle at top left,#020617,#020617);
}

.pub-index {
  font-size: 0.78rem;
  font-weight: 600;
  padding: 0.16rem 0.52rem;
  border-radius: 999px;
  background: #ffffff;
  color: var(--cv-accent);
  box-shadow: 0 0 0 1px rgba(37,99,235,0.16);
  margin-top: 0.1rem;
}

body[data-theme="dark"] .pub-index {
  background: #020617;
  color: #bfdbfe;
}

.pub-text {
  margin: 0;
  font-size: 0.94rem;
  line-height: 1.7;
}

/* ===== Others 信息块 ===== */
.info-block {
  border-radius: 16px;
  border: 1px solid var(--cv-border-soft);
  background: linear-gradient(135deg, #f9fafb, #ffffff);
  padding: 0.95rem 1.1rem;
  margin-top: 0.7rem;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.info-block:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(15, 23, 42, 0.08);
}

body[data-theme="dark"] .info-block {
  border-color: #1f2937;
  background: #020617;
}

.info-block-title {
  font-size: 0.98rem;
  font-weight: 600;
  color: var(--cv-text-main);
  margin-bottom: 0.3rem;
}

body[data-theme="dark"] .info-block-title {
  color: #e5e7eb;
}

.info-block-subtitle {
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--cv-text-muted);
  margin-bottom: 0.2rem;
}

.info-block ul {
  margin-top: 0.25rem;
  padding-left: 1.1rem;
}

/* Related Reports 链接样式 */
.cv-link-list {
  list-style: none;
  padding-left: 0;
  margin: 0.3rem 0 0;
  font-size: 0.9rem;
}

.cv-link-list li + li {
  margin-top: 0.2rem;
}

.cv-link-date {
  color: var(--cv-text-muted);
  margin-right: 0.35rem;
}

.cv-link-list a {
  color: var(--cv-accent);
  text-decoration: none;
  border-bottom: 1px dashed rgba(37,99,235,0.45);
}

.cv-link-list a:hover {
  border-bottom-style: solid;
}

/* Hobbies 列表 */
.cv-hobby-list {
  list-style: none;
  padding-left: 0;
  margin: 0.3rem 0 0;
}

.cv-hobby-list li + li {
  margin-top: 0.2rem;
}

/* 小块之间的整体间距 */
.cv-subsection-block {
  margin-top: 1rem;
}

/* 移动端适配 */
@media (max-width: 768px) {
  .cv-page {
    padding: 1.8rem 1.1rem 2.6rem;
  }
  .cv-section {
    padding: 1.4rem 1.25rem 1.3rem;
  }
}
</style>

<div class="cv-page">
<div class="cv-main">

<!-- ========== About Me ========== -->
<section class="cv-section" id="about-me" markdown="1">
<h2 class="section-title">About Me</h2>

<div style="text-align: justify;">

<p style="text-align: justify;">
  I am Yuhe Wu (吴宇赫), an undergraduate student in Economic Statistics at Dongbei University of Finance and Economics, expecting to graduate in July 2026. Currently, I'm conducting research at the Fintech Lab in the School of Fintech, supervised by <a href="https://sft.dufe.edu.cn/content_26950.html">Prof. Zhuang Liu</a>.
</p>
<p style="text-align: justify;">
  My research interests primarily focus on Artificial Intelligence in Finance, LLM self-evolution, LLM Reasoning and Data Generation, with an emphasis on improving the reliability, interpretability, and practical decision-making value of AI models in financial applications.
</p>

</div>
</section>

<!-- ========== Education ========== -->
<section class="cv-section" id="education" markdown="1">
<h2 class="section-title">Education</h2>

- *2022.09 - 2023.09*, Business Administration, Dongbei University of Finance and Economics (DUFE), Dalian.
- *2023.09 - Now*, Economic Statistics, Dongbei University of Finance and Economics (DUFE), Dalian.
</section>

<!-- ========== Research Experience ========== -->
<section class="cv-section" id="research-experience" markdown="1">
<h2 class="section-title">Research Experience</h2>

- *2025.06 - Now*, Research Assistant, **Fintech Thrust**, Hong Kong University of Science and Technology (Guangzhou).
- *2025.01 - 2025.07*, Research Assistant, **National Accounting Center**, Dongbei University of Finance and Economic.
- *2023.11 - Now*, Research Group Leader, **Fintech Lab**, Dongbei University of Finance and Economic. 
</section>

<!-- ========== Publication ========== -->
<section class="cv-section" id="publication">
  <h2 class="section-title">Publication</h2>

  <div class="pub-category" style="text-align: justify;">
    <h3 class="subsection-title">Journal Article</h3> 

    <ul class="pub-list">
      <li class="pub-item">
        <span class="pub-index">J1</span>
        <p class="pub-text"><strong>Yuhe Wu</strong>, Donghang Zheng, Yuran Chen, Shanshan Li, Yutong Zhang, Yueyao Ma, Miao Yu, Ruitong Liu, Wayne Lin, Zhuang Liu*, Xuhui Wang*. "HarmoniBERT:A Cross-Cultural Ensemble Learning Framework for ESG Text Annotation." In <strong>INFORMS Journal on Computing</strong>. [Under Review, UTD24]</p>
      </li>

      <li class="pub-item">
        <span class="pub-index">J2</span>
        <p class="pub-text"><strong>Yuhe Wu</strong>, Yuran Chen, Zhuang Liu*, Wayne Lin. "Enhancing Financial Decision-Making under Cyber Threats: A Dual-Branch Framework Integrating Bayesian Deep Learning and Explainable AI." In <strong>Annals of Operations Research</strong>. [Accepted, ABS3, JCR Q1]</p>
      </li>

      <li class="pub-item">
        <span class="pub-index">J3</span>
        <p class="pub-text">Zhuang Liu*, <strong>Yuhe Wu</strong>, Yuran Chen, Ruitong Liu, Yanning Dong, Jun Zhao. "通信-感知-计算融合：关键技术、挑战与未来趋势." In <strong>计算机科学与探索</strong>. [Accepted, CCF T2, 北大中文核心]</p>
      </li>
    </ul>
  </div>

  <div class="pub-category" style="margin-top: 1.1rem; text-align: justify;">
    <h3 class="subsection-title">Conference Paper</h3> 

    <ul class="pub-list">
      <li class="pub-item">
        <span class="pub-index">C1</span>
        <p class="pub-text">Jianing Hao, <strong>Yuhe Wu</strong>, Yuanjian Xu, Shichang MENG, Shuai Yuan, Wei Zeng, ZixuanWang, Guang Zhang*. "BizCompass: Benchmarking the Reasoning Capabilities of LLMs in Business Knowledge and Applications" In <strong>ACL 2026</strong>. [Under Review,CCF A]</p>
      </li>

      <li class="pub-item">
        <span class="pub-index">C2</span>
        <p class="pub-text"><strong>Yuhe Wu</strong>, Yuran Chen, Xinyue Su,Zhuang Liu*. "PolluVCCT: Multi-Scale Hybrid Learning for Robust Air Pollution Forecasting Across Diverse Climate Zonesti-source data Fusion." In <strong>KDD-UMC 2025</strong>. [Accepted,CCF A]</p>
      </li>
    </ul>
  </div>
</section>

<!-- ========== Others ========== -->
<section class="cv-section" id="others">
  <h2 class="section-title">Others</h2>

  <div class="info-block">
    <div class="info-block-title">Competition Awards</div>
    <div class="info-block-subtitle">National Level</div>
    <ul>
      <li><strong>Second Prize</strong>, <strong>9th Finance and Economics Innovation and Entrepreneurship Competition</strong> (第九届财经创新创业大赛), Team Leader, 2024</li>
      <li><strong>Third Prize</strong>, <strong>2024 10th National College Student Statistics Modeling Competition</strong> (2024第十届全国大学生统计建模大赛), Team Leader, 2024</li>
      <li><strong>Third Prize</strong>, <strong>3rd National ETF Elite Challenge</strong> (第三届全国ETF菁英挑战赛), Team Leader, 2025</li>
      <li><strong>National Level Completion</strong>, <strong>2024 National College Student Innovation and Entrepreneurship Training Program Project</strong> (2024大学生创新创业训练计划项目国家级), Project Leader, 2024</li>
      <li><strong>Bronze Award</strong>, <strong>2024 China International College Students' Innovation Competition</strong> (2024中国国际大学生创新大赛), Core Member (2/15), 2024</li>
      <li><strong>Third Prize</strong>, <strong>"Zheng Da Cup" 15th National College Student Market Research and Analysis Competition</strong> (“正大杯”第十五届全国大学生市场调查与分析大赛), Core Member (2/5), 2025</li>
      <li><strong>National Top 100</strong>, <strong>2024 "ICBC Cup" National College Student FinTech Innovation Competition</strong> (2024“工行杯”全国大学生金融科技创新大赛), Core Member (2/3), 2024</li>
    </ul>
  </div>

  <div class="info-block cv-subsection-block">
    <div class="info-block-title">Reviewer</div>
    <ul>
      <li>INFORMS Journal on Computing (UTD24)</li>
      <li>IEEE Transactions on Neural Networks and Learning Systems (Q1,中科院一区TOP)</li>
      <li>Journal of Business Research (Q1,中科院一区TOP，ABS3)</li>
      <li>Data Mining and Knowledge Discovery(Q2)</li>
      <li>ACL 2025(CCF A)</li>
      <li>KDD 2025(CCF A)</li>
      <li>ICDE 2025(CCF A)</li>
    </ul>
  </div>

  <div class="info-block cv-subsection-block">
    <div class="info-block-title">Honorable Awards</div>
    <ul>
      <li>First-Class Scholarship (2023，2024)，[2000 CNY]</li>
      <li>Third-Class Scholarship (2025)，[500 CNY]</li>
      <li>Merit Student (University Level) (2023, 2024)，[500 CNY]</li>
      <li>Dormitory Leader, Model Dormitory for Academic Atmosphere (2023), [1000 CNY]</li>
      <li>Excellent Individual in Innovation and Entrepreneurships (2024), [1000 CNY]</li>
      <li>Excellent Innovation and Entrepreneurship Team Scholarship (2025), [3920 CNY]</li>
      <li>Dashang Group Academic Research Scholarship, [5000 CNY]</li>
      <li>KDD-25 Undergraduate Scholarship(2025), [7000 CNY]</li>
      <li>Excellent Communist Youth League Member (2023)</li>
      <li>Advanced Individual in Academic Competitions (2025)</li>
    </ul>
  </div>
  
  <div class="info-block cv-subsection-block">
    <div class="info-block-title">Personal Skills</div>
    <p style="text-align: justify;">
      <strong>Large Language Models (LLMs).</strong>
      Proficient with mainstream text and multimodal LLMs (e.g., DeepSeek V3/R1, Qwen series, Llama series). Experienced with the full training pipeline from supervised fine-tuning (SFT) to reinforcement learning fine-tuning (RLFT/RLHF), with extensive hands-on experience in LLM API integration and model fine-tuning.
    </p>
    <p style="text-align: justify;">
      <strong>Econometrics, Programming & Modeling.</strong>
      Proficient in using SPSS, Stata, and SAS for econometric analysis and forecasting. Skilled in Python and R for data science. Familiar with deep learning frameworks such as PyTorch, Linux-based development environments, Conda environment management, and mathematical model implementation in Matlab.
    </p>
    <p style="text-align: justify;">
      <strong>Research & Software Proficiency.</strong>
      Proficient in LaTeX for scientific typesetting, Origin and Visio for academic plotting and diagramming, the Microsoft Office suite (Word, Excel, PowerPoint) for documentation and data analysis, and financial data terminals including Wind and Choice.
    </p>
    <p style="text-align: justify;">
      <strong>Bilingual Academic Writing.</strong>
      Proficient in academic writing in both Chinese and English, with practical experience in journal submissions and responding to reviewer comments.
    </p>
  </div>

  <div class="info-block cv-subsection-block">
    <div class="info-block-title">Hobbies</div>
    <ul class="cv-hobby-list">
      <li><strong>Guitar</strong>. I have a strong passion for playing the guitar, enjoying both learning songs.</li>
      <li><strong>Music</strong>. I am particularly fond of Hip-hop、K-POP and J-POP music.</li>
      <li><strong>Badminton</strong>. I enjoy playing badminton; it's a great way to stay active and have fun.</li>
    </ul>
  </div>

  <div class="info-block cv-subsection-block">
    <div class="info-block-title">Related Reports</div>
    <ul class="cv-link-list">
      <li><span class="cv-link-date">[2024.10]</span><a href="https://mp.weixin.qq.com/s/KJB5Vp7P_2t2fpfDNZeCeg">[国创赛，点亮上海！]</a></li>
      <li><span class="cv-link-date">[2025.01]</span><a href="https://mp.weixin.qq.com/s/pLgP7S5XFyFv0l8EI0Gxpg">[东北财经大学师生参加全国财经院院校创新创业联盟2024年年会暨第九届全国大学生创新创业大赛并获奖]</a></li>
      <li><span class="cv-link-date">[2025.04]</span><a href="https://mp.weixin.qq.com/s/x5oWQ3uGy37ac8klV-a6Xw">[2025年辽宁省普通高等学校本科大学生市场调查与分析大赛暨“正大杯”第十五届全国大学生市场调查与分析大赛辽宁赛区选拔赛成功举办]</a></li>
    </ul>
  </div>
</section>

<!-- ========== Startup Project ========== -->
<section class="cv-section" id="startup-projects" markdown="1">
<h2 class="section-title">Startup Project</h2>

<h4>💪 Upcoming Project</h4>
</section>

</div>
</div>
