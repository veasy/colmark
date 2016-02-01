'use strict';

angular.module('colmark', [])

.controller('MainController', function($scope) {
	angular.element(document).ready(function () {


		function Editor(input, preview) {
			this.update = function () {
				preview.innerHTML = markdown.toHTML(input.value);
			};
			this.update();
		}
		new Editor($("#editor"), $("#preview"));

		console.log("init");
	});
});