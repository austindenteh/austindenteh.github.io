```{=html}
<div class="observation-map" role="group" aria-label="Mapping potential treatment choices and outcomes to one observed data row">
  <p class="observation-map-title">One person. Two possible paths. One observed row.</p>
  <div class="potential-card">
    <p class="map-card-heading">Full information: known to us in this simulation</p>
    <div class="potential-pairs">
      <p><strong>Treatment choices</strong><br><var>D</var>(0) = 0 &nbsp; · &nbsp; <var>D</var>(1) = 1</p>
      <p><strong>Potential outcomes</strong><br><var>Y</var>(0) = 1 &nbsp; · &nbsp; <var>Y</var>(1) = 4</p>
    </div>
    <p class="map-detail">This person is a <span class="compliance-type type-complier">complier</span>. Their effect is 4 − 1 = 3.</p>
  </div>
  <div class="offer-path unrealized-path">
    <p class="path-label">Alternative but unrealized path for person: no offer received — researcher does not see this path</p>
    <div class="path-sequence">
      <div><strong><var>Z</var> = 0</strong><br>No offer</div>
      <span class="path-arrow" aria-hidden="true">→</span>
      <div><strong><var>D</var> = <var>D</var>(0) = 0</strong><br>No treatment</div>
      <span class="path-arrow" aria-hidden="true">→</span>
      <div><strong><var>Y</var> = <var>Y</var>(0) = 1</strong><br>Outcome without treatment</div>
    </div>
  </div>
  <div class="offer-path realized-path">
    <p class="path-label">Realized path: offer received — researcher sees this path</p>
    <div class="path-sequence">
      <div><strong><var>Z</var> = 1</strong><br>Offer</div>
      <span class="path-arrow" aria-hidden="true">→</span>
      <div><strong><var>D</var> = <var>D</var>(1) = 1</strong><br>Treatment</div>
      <span class="path-arrow" aria-hidden="true">→</span>
      <div><strong><var>Y</var> = <var>Y</var>(1) = 4</strong><br>Outcome with treatment</div>
    </div>
    <p class="observed-row"><span>What the researcher sees</span><br><strong>(<var>Z</var>, <var>D</var>, <var>Y</var>) = (1, 1, 4)</strong></p>
    <p class="map-detail">The observed row alone could come from a <span class="compliance-type type-complier">complier</span> or an <span class="compliance-type type-always-taker">always-taker</span>. Seeing both paths in this illustration does not give the researcher a second observation.</p>
  </div>
  <div class="hidden-card">
    <p><strong>What the researcher still cannot see</strong><br><var>D</var>(0), <var>Y</var>(0), the individual effect, and this person’s type.</p>
  </div>
</div>
```
