attr = DS.attr;

GitView.Repository = DS.Model.extend({
    owner: attr("string"),
    name: attr("string"),
    isPublic: attr("boolean"),
    hasIssues: attr("boolean"),
    defaultBranch: attr("string")
});
