<div class="report">
  <h2>Procedure</h2>
  <ol>
    <li>One chat per unit, in the Learning Project. Copy the unit's brief from this course's Briefs page and paste it into a new chat; never reuse a chat across units. An isolated agent context counts as a chat (method.md §4, P31).</li>
    <li>The unit is written in full with its deliverable and its figures, each figure a fenced <code>viz</code> block of a kind <code>kit/viz.py</code> can draw. Every Perqo fact the unit invents is labelled and kept consistent with the Perqo facts already filed.</li>
    <li>A fresh checker in a new context that has not seen the writing (Opus 5.5, <code>skills/audit-units</code> §3) checks every cited claim and every figure's content against the unit, and the deliverable against the brief; findings are applied as exact replacements and the report filed as <code>audits/ux/fresh-check-&lt;code&gt;.md</code>.</li>
    <li>File the unit at <code>courses/ux/&lt;code&gt;-&lt;slug&gt;.md</code> with the front matter of method.md §7 (<code>skills/file-unit</code>); update this data file, rebuild, verify, publish Academy.</li>
  </ol>
  <h2>Models</h2>
  <ul>
    <li><strong>Writing: Opus 5.5</strong> for every unit. The deliverable is written in the same chat as its unit.</li>
    <li><strong>Checking: Opus 5.5</strong>, a fresh context each time, before filing; the model that checked each filed unit is on How it was built.</li>
    <li><strong>Not Sonnet or Haiku</strong> for units or checks.</li>
  </ul>
</div>
<section class="howto edge" style="--hc:var(--gold)"><h2>Review rule</h2>
  <p>Every new unit gets its fresh check before filing: every cited claim against its source, the deliverable against the brief. Figures count as claims: each figure is checked for whether its labels and numbers match the unit's sourced text. Units written with live search (DD-IA1, DD-IA2) are re-checked for staleness six months after writing.</p>
</section>
