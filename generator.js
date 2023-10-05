console.log('dsd');

var arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];
var arr3 = ['a', 'b', 'c', 'd'];

document.getElementById('param-1').oninput = function () {
	console.log(this.value);
	document.getElementById('password-length').innerHTML = this.value;
}
