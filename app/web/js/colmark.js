'use strict';

angular.module('colmark', [])

.controller('MainController', function($scope) {
	var generateId = function()
	{
		var text = "";
		var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

		for( var i=0; i < 5; i++ )
			text += possible.charAt(Math.floor(Math.random() * possible.length));

		return text;
	};
	var socket = io.connect('/document');

	socket.emit('/join',{
		username: generateId(),
		document: 'co234k688'
	});

	angular.element(document).ready(function () {
		function Editor(input, preview) {
			this.update = function () {
				preview.innerHTML = markdown.toHTML(input.innerHTML.replace(/&nbsp;/,"").replace(/<br>/ig,"\n").replace(/(<([^>]+)>)/ig,""));
			};
			this.update();
		}
		var byId = function (id) { return document.getElementById(id); };
		var editor = new Editor(byId("editor"), byId("preview"));

		document.getElementById("editor").addEventListener("input", function() {
			editor.update();
			socket.emit('/add',{
				position: 1,
				add: 'a',
				document: 'co234k688'
			});
		}, false);
	});
});