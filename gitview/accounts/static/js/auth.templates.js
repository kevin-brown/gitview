Ember.TEMPLATES["login"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [4,'>= 1.0.0'];
helpers = this.merge(helpers, Ember.Handlebars.helpers); data = data || {};
  var buffer = '', stack1, helper, options, escapeExpression=this.escapeExpression, helperMissing=helpers.helperMissing, self=this;

function program1(depth0,data) {
  
  
  data.buffer.push("\n        Sign in\n    ");
  }

  data.buffer.push("<form ");
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "authenticate", {hash:{
    'on': ("submit")
  },hashTypes:{'on': "STRING"},hashContexts:{'on': depth0},contexts:[depth0],types:["STRING"],data:data})));
  data.buffer.push(" class=\"auth-form\">\n    <label for=\"id_identification\">\n        Username:\n    </label>\n\n    ");
  data.buffer.push(escapeExpression((helper = helpers.input || (depth0 && depth0.input),options={hash:{
    'type': ("text"),
    'id': ("id_identification"),
    'class': ("form-control"),
    'value': ("identification")
  },hashTypes:{'type': "STRING",'id': "STRING",'class': "STRING",'value': "ID"},hashContexts:{'type': depth0,'id': depth0,'class': depth0,'value': depth0},contexts:[],types:[],data:data},helper ? helper.call(depth0, options) : helperMissing.call(depth0, "input", options))));
  data.buffer.push("\n\n    <label for=\"id_password\">\n        Password:\n    </label>\n\n    ");
  data.buffer.push(escapeExpression((helper = helpers.input || (depth0 && depth0.input),options={hash:{
    'type': ("password"),
    'id': ("id_password"),
    'class': ("form-control"),
    'value': ("password")
  },hashTypes:{'type': "STRING",'id': "STRING",'class': "STRING",'value': "ID"},hashContexts:{'type': depth0,'id': depth0,'class': depth0,'value': depth0},contexts:[],types:[],data:data},helper ? helper.call(depth0, options) : helperMissing.call(depth0, "input", options))));
  data.buffer.push("\n\n    ");
  stack1 = (helper = helpers['bs-button'] || (depth0 && depth0['bs-button']),options={hash:{
    'type': ("success")
  },hashTypes:{'type': "STRING"},hashContexts:{'type': depth0},inverse:self.noop,fn:self.program(1, program1, data),contexts:[],types:[],data:data},helper ? helper.call(depth0, options) : helperMissing.call(depth0, "bs-button", options));
  if(stack1 || stack1 === 0) { data.buffer.push(stack1); }
  data.buffer.push("\n</form>\n");
  return buffer;
  
});