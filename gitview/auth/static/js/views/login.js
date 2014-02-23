GitView.LoginFormView = Ember.View.extend({
    tagName: "form",
    classNames: ["auth-form"],

    username: null,
    password: null,

    submit: function (event) {
        event.preventDefault();

        console.log(this);

        this.authenticate();

        var username = this.get("username");
        var password = this.get("password");

        var data = {
            username: username,
            password: password
        };

        $.ajax({
            url: "/api/login",
            data: data,
            type: "POST"
        }).always(function (something) {
            if (something.responseJSON) {
                var response = something.responseJSON;

                Bootstrap.NM.push(response.message, "danger");
            } else {
                var response = something;

                Bootstrap.NM.push(response.message, "success");

                window.location = "/";
            }
        });
    }
});
