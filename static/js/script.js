'use strict';

// Select form elements
const form = document.querySelector('form');
const guestsInput = document.querySelector('#guests');
const topicsInput = document.querySelector('#topics');

// Select generated script element
const generatedScriptEl = document.querySelector('#generated-script');

// Add event listener for form submission
form.addEventListener('submit', (event) => {
  event.preventDefault();

  // Get input values from form
  const guests = guestsInput.value;
  const topics = topicsInput.value;

  // Generate script using input values
  const script = generateScript(guests, topics);

  // Update generated script element with new content
  generatedScriptEl.innerHTML = script;
});

// Function for generating podcast script based on guest names and topics
function generateScript(guests, topics) {
  return `Welcome back to "Never Say Die," everyone! Today we have ${guests} joining us as we discuss ${topics}. Let's get started!

${guests}: Thanks for having us.

Host: So, ${guests}, tell us about your experience working on [related project or topic].

${guests}: It was such an amazing experience. We really enjoyed working with [related people or companies], and we learned so much along the way.

Host: That's great to hear. And what about you, [other guest]? What was your favorite part of working on this project?

[Other guest]: I would have to say my favorite part was [related task or aspect]. It was challenging but also very rewarding.

Host: Fascinating. Now let's move on to our next topic...

[continue conversation]`;
}