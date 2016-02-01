'use strict';

angular.module('colmark', [])

.controller('MainController', function($scope) {
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
	});
});