[QueryItem="12"]
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX dicp: <https://w3id.org/digitalconstruction/0.5/Processes#>
PREFIX dica: <https://w3id.org/digitalconstruction/0.5/Agents#>
PREFIX dice: <https://w3id.org/digitalconstruction/0.5/Entities#>
PREFIX ocqa: <https://w3id.org/ocqa#> 
PREFIX ocqa-screed: <https://w3id.org/ocqa-screed#>
PREFIX ocqa-reg: <https://w3id.org/ocqa-regulation#>
PREFIX ocqa-con: <https://w3id.org/ocqa-contract#>
PREFIX ocqa-cat: <https://w3id.org/ocqa-catalog#>
PREFIX so: <https://schema.org/>
PREFIX : <https://example.de/ocqa-screed-inspections#>

SELECT ?x
WHERE {ocqa-screed:FlatnessInspection dice:hasEquipment ?x.
}