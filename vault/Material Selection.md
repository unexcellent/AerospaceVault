#uni/courses/materials 

Due to the widely different properties of [[Material|materials]] a wide range of methods have been developed to select the right one for the task.

![[Pasted image 20240630131320.png]]

# Connections to the Part Design Process

- The type of material information changes massively during the material selection process 
- The type of information needed can be highlighted when connecting the material selection process to the part design process

![[Pasted image 20240630131524.png|200]]

## Concept Design

- Approximate material property data is needed, but preferably for all materials
- Quick access to the information and breadth are of interest, detail and precision are not
- Whether to use innovative materials has to be determined in this stage

## Embodiment Design

- More detailed data is needed for a subset of materials (only titanium alloys, only polymers, etc.)
- Risk of “getting stuck” in a single material class
- General handbooks or software for material classes give a good overview
- The approximate size and shape of the part is determined in this stage

## Detail Design

 - The maximum amount of information is needed for a single (or very few) material(s)
 - The same materials from different manufacturers can have different properties
 - If it is a critical part -> conducting tests with this specific material might be necessary
 - The specifications are determined and accompanied by a documentation

# Selection Process

- Four main steps to get from the domain of all materials to the final material choice 
- The domain of all materials has to be complete and of high quality -> prevent excluding a material a priori because of a lacking database

## Translation

“How are the design requirements for a component (defining what it must do) translated into a prescription for a material?"

Every part has a **function** that has to be fulfilled under certain **constraints** whilst taking multiple objectives **into** account. The objectives can be optimised by varying the **free variables**.

### Functions

Examples for functions: carry load, limit deflection, conduct heat, withstand an internal/ external pressure, ...

### Constraints

Examples for constraints: limited building space, operation temperature range, corrosion resistance, ...

### Objectives

Examples for objectives: minimise costs, minimise weight, maximise safety or a combination of those

## Screening

Eliminate materials that cannot do the job.

## Ranking

Find the screened materials that do the job best.

- After all inadmissible materials have been rejected 
- Rank the remaining materials based on objective metric -> material performance indices 
- Identify the materials that can fulfil their function best

## Seek Documentation

Research the family history of top-ranked candidates