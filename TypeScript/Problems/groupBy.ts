/**
 * Given a list of objects, group them by a the 'type' key and return the total funding for each type.
 *
 * The trick here is to use the array's reduce method, the accumulator here is an object
 * (typed the same as the return type). We use the project type as the object key, and
 * check if that type already exists (else zero) and add the new project's funding to that key-value.
 * One last note, we need to pass in an empty object as the initial value (2 arg to reduce)
 * or it'll use the first object in the array and include all it's properties (including 'name', 'type', etc.).
 */
type Project = { name: string; type: string; funding: number };

const projects: Project[] = [
  { name: "Solar Farm", type: "solar", funding: 100 },
  { name: "Wind Farm", type: "wind", funding: 150 },
  { name: "Battery Storage", type: "battery", funding: 75 },
  { name: "Solar Expansion", type: "solar", funding: 120 },
];

// Write a function that returns the total funding per project type as a record
// Output: { solar: 220, wind: 150, battery: 75 }
function getFundingByType(projects: Project[]): Record<string, number> {
    return projects.reduce((acc, project) => {
        acc[project.type] = (acc[project.type] || 0) + project.funding;
        return acc;
    }, {});
}

console.log(getFundingByType(projects))