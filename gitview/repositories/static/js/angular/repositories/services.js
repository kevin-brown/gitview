GitView.repositories.factory("Repository",
["Commit", "$http", function(Commit, $http)
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

             if (!self.tree)
             {
                 self.getTree(response.data.default_branch);
             }
         });
     }

     Repository.prototype.getCommit = function (hash)
     {
         var self = this;

         request = $http.get(self.apiUrl + "commits/" + hash);

         request.then(function (response)
         {
             self.commit = response.data;
         });

         return request;
     };

     Repository.prototype.getTree = function (tree, treePath)
     {
         var self = this;

         self.tree = true;

         var url = self.apiUrl + "trees/" + tree;

         if (treePath)
         {
             url = url + "/" + treePath;
         }

         $http.get(url).then(function (response)
         {
             self.tree = response.data;

             self.tree.commit = Commit.get(self, response.data.commit_hash);

             $.each(self.tree.trees, function ()
             {
                 this.commit = Commit.get(self, this.commit_hash);
             });

             $.each(self.tree.blobs, function ()
             {
                 this.commit = Commit.get(self, this.commit_hash);
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


GitView.repositories.factory("Commit",
[function()
 {
     function Commit(repository, hash, request)
     {
         var self = this;

         request.then(function(response)
         {
             self.hash = response.data.hash;

             self.summary = response.data.summary;
             self.description = response.data.description;

             self.committedTime = response.data.committed_time;

             self.commitUrl = repository.rootUrl + "commits/" +
                 self.hash;
         });
     }

     var commit = {
         get: function(repository, hash) {
             request = repository.getCommit(hash);

             return new Commit(repository, hash, request);
         }
     };

     return commit;
 }]);
