var SpeechRecognition = window.webkitSpeechRecognition;

var recognition = new SpeechRecognition();

var Textbox = $("#textbox");
var instructions = $("instructions");

var Content = "";

recognition.continuous = true;

recognition.onresult = function (event) {
  var current = event.resultIndex;

  var transcript = event.results[current][0].transcript;

  Content += transcript;
  Textbox.val(Content);
};

recognition.onstart = function () {
  instructions.text("Voice recognition is ON.");
};

recognition.onspeechend = function () {
  instructions.text("No activity.");
};

recognition.onerror = function (event) {
  if (event.error == "no-speech") {
    instructions.text("Try again.");
  }
};

$("#start-btn").on("click", function (e) {
  if (Content.length) {
    Content += " ";
  }
  recognition.start();
});

Textbox.on("input", function () {
  Content = $(this).val();
});
