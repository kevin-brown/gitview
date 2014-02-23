GitView.Router.reopen({
    location: "history"
});

GitView.Router.map(function () {
    this.route("login");
    this.route("logout");
    this.resource("repository", {
        path: "/:owner_name/:repository_name"
    });
    this.resource("owner", {
        path: "/:owner_name"
    });
});

GitView.IndexRoute = Ember.Route.extend({
    beforeModel: function () {
        if (!GitView.User.loggedIn) {
            this.transitionTo("login");
        }
    }
});

GitView.LoginRoute = Ember.Route.extend({
    beforeModel: function () {
        if (GitView.User.loggedIn) {
            this.transitionTo("index");
        }
    }
});

GitView.RepositoryRoute = Ember.Route.extend({
    model: function (params) {
        return Ember.$.getJSON("/api/repositories/%@/%@".fmt(params.owner_name, params.repository_name));
    },
    renderTemplate2: function () {
        this._super(this, arguments);
        this.render("a", {
            outlet: "b",
            into: "a"
        });
    }
});
