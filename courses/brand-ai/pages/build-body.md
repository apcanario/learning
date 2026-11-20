<div class="report">
  <h2>Procedure</h2>
  <ol>
    <li>Make a Project ("Courses — Brand &amp; AI"). Add to its knowledge: this page, the research report, the five notes files. Project instructions, three lines: who the reader is; this page holds every brief; each unit is written in full, not described.</li>
    <li>One chat per unit. Copy the unit's brief from its Briefs page, paste it into a new chat in that Project. Never reuse a chat across units; leaked context is how a course starts repeating itself.</li>
    <li>Save the output to the vault as <code>courses/brand-ai/&lt;code&gt;-&lt;slug&gt;.md</code> (e.g. <code>B1-mental-model.md</code>), same shape as the history course. Hand it to the assistant: it commits, adds the unit to Learn, moves the counters, adds a changelog line.</li>
    <li>Units that need live facts (A8, B2, B8, DD-A1, DD-B3) are written with web search on; the briefs say so. Everything else without.</li>
  </ol>
  <h2>Models</h2>
  <ul>
    <li><strong>Writing: Opus 5.5</strong> for all remaining units. The quality gap shows most on long-form synthesis, which is this.</li>
    <li><strong>The shipped deliverable</strong> is written in the same chat as its unit, never separately, so it inherits the unit's reasoning.</li>
    <li><strong>Checking: a fresh context</strong> that has not seen the writing checks every cited claim against its source before the unit is filed (Fable 5.1 to A4, Opus 5.5 from A5).</li>
    <li><strong>Not Sonnet or Haiku</strong> for units or checks. They are the right tools for turning a finished unit into posts, a Shorts list or an email; that is B7's pipeline.</li>
  </ul>
</div>
<section class="howto edge" style="--hc:var(--gold)"><h2>Review rule</h2>
  <p>Every unit gets a fresh check before filing: every cited claim against its source, the deliverable against the brief. Units written with live search (the Search column of <code>courses-index.md</code> lists them) are re-checked for staleness six months after writing.</p>
</section>
