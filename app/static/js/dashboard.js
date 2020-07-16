window.onload = function(obj) {	

	function fadeOutEffect() {
	    var fadeTarget = document.getElementById("alert-success");
	    var fadeEffect = setInterval(function () {
	        if (!fadeTarget.style.opacity) {
	            fadeTarget.style.opacity = 1;
	        }
	        if (fadeTarget.style.opacity > 0) {
	            fadeTarget.style.opacity -= 0.1;
	        } else {
	            clearInterval(fadeEffect);
	        }
	    }, 200);
	}

fadeOutEffect()
}