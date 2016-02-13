'use strict';

angular.module('colmark', [])

.controller('MainController', function($scope, Utility) {
	var socket = Utility.connect();
	var editor;

	socket.emit('join',{
		username: Utility.generateId(),
		document: 'co234k688'
	});

	socket.on('update', function(update) {
		console.log('update ', update);
		var editorDiv = document.getElementById("editor");
		editorDiv.innerHTML += update;
		editor.update();
	});

	angular.element(document).ready(function () {
		function Editor(input, preview) {
			this.update = function () {
				preview.innerHTML = markdown.toHTML(input.innerHTML.replace(/&nbsp;/,"").replace(/<br>/ig,"\n").replace(/(<([^>]+)>)/ig,""));
			};
			this.update();
		}
		var byId = function (id) { return document.getElementById(id); };
		editor = new Editor(byId("editor"), byId("preview"));

		document.getElementById("editor").addEventListener("input", function(e) {

		}, false);
	});

	var keydownListener;

	var getCharFromKeyCode = function(keyCode) {
		if (keyCode === 8) return 'delete';
		if (keyCode === 13) return 'enter';
		if (keyCode === 32) return 'space';

		return String.fromCharCode(keyCode);
	};

	$scope.editorFocus = function() {
		keydownListener = document.addEventListener('keydown', function(e) {
			console.log('keydown', getCharFromKeyCode(e.keyCode));
			var editorDiv = document.getElementById("editor");
			editor.update();
			socket.emit('add',{
				position: editorDiv.innerHTML.length,
				add: getCharFromKeyCode(e.keyCode),
				document: 'co234k688'
			});
		})
	};

	$scope.editorBlur = function() {
		document.removeEventListener(keydownListener);
	};
})

.factory('Utility', function() {
	return {
		connect: function() {
			return io.connect('/document');
		},
		generateId: function() {
			var text = "user-";
			var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

			for( var i=0; i < 5; i++ )
				text += possible.charAt(Math.floor(Math.random() * possible.length));

			return text;
		}
	};
});