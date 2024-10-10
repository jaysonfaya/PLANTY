document.addEventListener("DOMContentLoaded", function() {
    const plantTypeSelect = document.getElementById("plant-type-select");
    const plantNameInput = document.getElementById("plant-name-input");
    const nameSubmitButton = document.getElementById("name-submit-button");
    const plantImage = document.getElementById("plant-image");
    const waterButton = document.getElementById("water-button");
    const repotButton = document.getElementById("repot-button");
    const sunButton = document.getElementById("sun-button");
    const fertilizeButton = document.getElementById("fertilize-button");
    const pruneButton = document.getElementById("prune-button");
    const fastForwardButton = document.getElementById("fast-forward-button");
    const plantNameDisplay = document.getElementById("plant-name");
    const toast = document.getElementById("toast");
    const taskLog = document.getElementById("task-log");

    let currentPlantType = "fern";

    // Überprüfung der Elemente
    const elements = { plantTypeSelect, plantNameInput, nameSubmitButton, plantImage, waterButton, repotButton, sunButton, fertilizeButton, pruneButton, fastForwardButton, plantNameDisplay, toast };
    for (const [key, value] of Object.entries(elements)) {
        if (!value) {
            console.error(`Element "${key}" wurde im DOM nicht gefunden.`);
            return;
        }
    }

    function showToast(message) {
        toast.textContent = message;
        toast.classList.remove("hidden");
        setTimeout(function() {
            toast.classList.add("hidden");
        }, 3000);
    }

    function logTask(message) {
        const logItem = document.createElement("li");
        logItem.textContent = message;
        taskLog.appendChild(logItem);
    }

    plantTypeSelect.addEventListener("change", function() {
        currentPlantType = plantTypeSelect.value;
    });

    nameSubmitButton.addEventListener("click", function() {
        const plantName = plantNameInput.value.trim();
        if (plantName) {
            plantNameDisplay.textContent = plantName;
            showToast("Pflanze benannt!");
            logTask(`Pflanze benannt: ${plantName}`);
            document.querySelectorAll(".control-button").forEach(button => {
                button.style.display = "inline-block";
            });
        } else {
            showToast("Bitte gib deiner Pflanze einen Namen.");
        }
    });

    repotButton.addEventListener("click", function() {
        showToast("Samen eingetopft!");
        plantImage.src = `images/potted_seed_${currentPlantType}.png`;
        repotButton.style.display = "none";
        waterButton.style.display = "inline-block";
        logTask("Samen eingetopft.");
    });

    waterButton.addEventListener("click", function() {
        showToast("Die Pflanze wurde gegossen!");
        plantImage.src = `images/young_${currentPlantType}.png`;
        waterButton.style.display = "none";
        sunButton.style.display = "inline-block";
        logTask("Pflanze gegossen.");
    });

    sunButton.addEventListener("click", function() {
        showToast("Die Pflanze erhält Sonnenlicht!");
        plantImage.src = `images/${currentPlantType}.png`;
        sunButton.style.display = "none";
        pruneButton.style.display = "inline-block";
        logTask("Sonnenlicht gegeben.");
    });

    pruneButton.addEventListener("click", function() {
        showToast("Die Pflanze wurde geschnitten!");
        pruneButton.style.display = "none";
        fertilizeButton.style.display = "inline-block";
        logTask("Pflanze geschnitten.");
    });

    fertilizeButton.addEventListener("click", function() {
        showToast("Die Pflanze wurde gedüngt!");
        plantImage.src = `images/full_${currentPlantType}.png`;
        fertilizeButton.style.display = "none";
        logTask("Pflanze gedüngt.");
    });

    fastForwardButton.addEventListener("click", function() {
        showToast("Schnellvorlauf aktiviert!");
        simulateFastForward();
    });

    function simulateFastForward() {
        setTimeout(function() {
            showToast("Pflanze wächst schneller!");
            plantImage.src = `images/full_${currentPlantType}.png`;
            logTask("Schnellvorlauf aktiviert.");
        }, 2000);
    }
});
