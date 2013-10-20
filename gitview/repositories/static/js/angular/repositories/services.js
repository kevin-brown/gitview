GitView.repositories.factory("Repository",
["$http", function($http)
 {
     function Repository(ownerName, repositoryName, request)
     {
         var self = this;

         self._request = request;

         self.loaded = request.then;

         self.owner = ownerName;

         self.ownerUrl =  "/" + ownerName + "/";
         self.rootUrl = self.ownerUrl + repositoryName + "/";
         self.filesUrl = self.rootUrl;
         self.commitsUrl = self.rootUrl + "commits"

         self.apiUrl = "/api/repositories" + self.rootUrl;

         request.then(function (response)
         {
             self.name = response.data.name;
             self.isPublic = response.data.is_public;
             self.hasIssues = response.data.has_issues;

             self.getTree(response.data.default_branch);
         });
     }

     Repository.prototype.getTree = function (tree, treePath)
     {
         var self = this;

         $http.get(self.apiUrl + "trees/" + tree).then(function (response)
         {
             self.tree = response.data;

             $.each(self.tree.trees, function ()
             {
                 this.commit = {
                     summary: "Commit summary",
                     committed_time: "That time"
                 };
             });
         });
     };

     var repository = {
         get: function(ownerName, repositoryName) {
             request = $http.get("/api/repositories/" + ownerName + "/" +
                                 repositoryName);

             return new Repository(ownerName, repositoryName, request);
         }
     };

     return repository;
 }]);
