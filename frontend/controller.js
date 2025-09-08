$(document).ready(function () {
	// Display the spoken text in the frontend
	eel.expose(DisplayMessage)
	function DisplayMessage(text) {
		$('.siri-message li:first').text(message);
		$('.siri-message').textillate('start');
	}

	
});