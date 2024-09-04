#uni/courses/cad 
-> [[Technical Drawings]]
# Sections

- Purpose of sections is to reveal internal details like bores, internal threads, grooves, etc.
- Hidden elements cannot be [[Dimensioning|dimensioned]], thus the need for sections
- Section planes in 3D become section lines in the views (more details follow)

## Properties of Hatching

- Hatching lines are:
	- narrow, full lines
	- at an angle of 45º to the relevant body contour, or to the symmetry line of the component
	- spacing of the lines is even and constant

- A part always has the same hatching in all views!
	- Same direction and same spacing of hatching lines
	- The hatching is not turned when rotating a view

- If a drawing contains several sectioned parts, then the different parts are given different hatching.
	- Opposing hatching direction and/or other spacing
	- Part A: Hatching (1) with angle (2) and spacing (3)
	- Part B: Hatching (4) with angle (5) and spacing (6)

## Types of Sections

### Full Section

### Half Section

allowed only for rotationally symmetrical components (e.g. drive shafts)

### Part Section

only allowed if the sectioned part is dimensioned elsewhere

## Projection rules & sections

- The projection rules of the drawing are not applied to sections
- A section does not replace a view (the arrow method applies)
- Sections must not be placed between (projected) views.
- Half- and part-sections are, however, allowed within the views (they are perceived as a view)

## Positioning and designation of sections

Designation of the cutting line by
- Broad dashed-dotted line that slightly overlaps with component
- Section arrows (30° apex angle)
- Capital letters (one font size higher than for dimensions):
	- Line group 0,5: Dimension font size 3.5mm, Section letter 5mm
- Section is placed on drawing in arrow direction



Cutting line with parallel offset planes
- Designation of the cutting line as above (Broad dashed-dotted line)
- Broad full lines at the kinks
- No edge in the section at kinks in section line when inside the part

Oblique cutting line:
- Designation of the section progression as above (Broad dashed-dotted line, broad full line at the kinks)
- View always in the direction of the arrow, i.e.
	- Real length along the cutting line is NOT represented,
	- only the projected line (length) is drawn!

Angled cutting line
- Designation of the cutting line as above
- Projection according to reading direction (first top down, then from left to the right)

Cutting line partly outside the component:
- Designation of the cutting line transition by broad full line
- Intersection with component outer boundary is a solid broad line

Section not arranged according to the arrow direction
Additional designation by…
- Direction of rotation
- Angle
