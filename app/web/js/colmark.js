'use strict';

angular.module('colmark', [])

.controller('MainController', function($scope) {
	makeid = function()
	{
		var text = "";
		var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

		for( var i=0; i < 5; i++ )
			text += possible.charAt(Math.floor(Math.random() * possible.length));

		return text;
	}

	angular.element(document).ready(function () {


		function Editor(input, preview) {
			this.update = function () {
				preview.innerHTML = markdown.toHTML(input.innerHTML.replace(/&nbsp;/,"").replace(/<br>/ig,"\n").replace(/(<([^>]+)>)/ig,""));
			};
			this.update();
		}
		var byId = function (id) { return document.getElementById(id); };
		var editor = new Editor(byId("editor"), byId("preview"));

		console.log("init");

		document.getElementById("editor").addEventListener("input", function() {
			editor.update();
		}, false);

		var socket = io.connect('/join',{
			username: makeid(),
			document: 'co234k688'
		});
	});
});