Ember.Application.initializer({
    name: 'authentication',
    initialize: function(container, application) {
        Ember.SimpleAuth.setup(application);
    }
});

var GitView = Ember.Application.createWithMixins(Bootstrap.Register);

GitView.Authenticator = Ember.SimpleAuth.Authenticators.OAuth2.extend({
    serverTokenEndpoint: "/oauth/token"
});
