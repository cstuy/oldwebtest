

var templatedata='{{#each person}}<li class="span2"><div class="thumbnail"> <img data-src="/media/about/{{photo}}"> <h3>{{name}}</h3></div></li>{{/each}}';

var template=Handlebars.compile(templatedata);
