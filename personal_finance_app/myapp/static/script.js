$(document).ready(function () {
    // Function to calculate and set the progress for each goal
    function updateGoalProgressBars() {
        $(".goal-card").each(function () {
            // Get saved and total values from data attributes
            const saved = parseFloat($(this).data("saved"));
            const total = parseFloat($(this).data("total"));

            // Calculate the percentage
            const percentage = (saved / total) * 100;

            // Update the progress bar width and text
            $(this).find(".progress-bar")
                .css("width", `${percentage}%`)
                .attr("aria-valuenow", percentage) // Update ARIA attribute for accessibility
                .text(`${Math.round(percentage)}%`);
        });
    }

    // Call the function to update individual progress bars
    updateGoalProgressBars();

    // Function to calculate total progress for circle bar
    function calculateTotalProgress() {
        let totalSaved = 0;
        let totalRequired = 0;

        // Iterate over all goal cards
        $(".goal-card").each(function () {
            const saved = parseFloat($(this).data("saved"));
            const total = parseFloat($(this).data("total"));

            totalSaved += saved;
            totalRequired += total;
        });

        // Calculate the progress percentage
        const progressValue = totalSaved / totalRequired;

        // Update the circle progress bar
        $('#example').circleProgress({
            size: 230,
            value: progressValue,
            background: 'transparent',
            fill: {
                color: '#ffffff'
            },
            thickness: 25
        });

        // Optionally update the displayed saved amount
        $("p").text(`${totalSaved} RON saved`);
    }

    // Call the function to update total progress
    calculateTotalProgress();
});
