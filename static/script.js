// Function to send the user's message
async function sendMessage() {

    // Get the input box
    const input = document.getElementById("user-input");

    // Get the text entered by the user
    const message = input.value.trim();

    // If input is empty, do nothing
    if (message === "") {
        return;
    }

    // Get the chat box
    const chatBox = document.getElementById("chat-box");

    // Display the user's message
    chatBox.innerHTML += `
        <div class="user-message">
            ${message}
        </div>
    `;

    // Clear the input box
    input.value = "";

    // Scroll to the latest message
    chatBox.scrollTop = chatBox.scrollHeight;

    try {

        // Send the message to Flask
        const response = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });

        // Convert response into JSON
        const data = await response.json();

        // Display chatbot reply
        chatBox.innerHTML += `
            <div class="bot-message">
                ${data.reply}
            </div>
        `;

        // Scroll to latest message
        chatBox.scrollTop = chatBox.scrollHeight;

    } catch (error) {

        chatBox.innerHTML += `
            <div class="bot-message">
                Something went wrong.
            </div>
        `;

    }

}

// Press Enter to send message
document.getElementById("user-input").addEventListener("keypress", function(event){

    if(event.key === "Enter"){

        sendMessage();

    }

});
