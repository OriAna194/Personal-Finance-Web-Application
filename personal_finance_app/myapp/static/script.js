$(document).ready(function () {
    
    function updateGoalProgressBars() {
        $(".goal-card").each(function () {
            
            const saved = parseFloat($(this).data("saved"));
            const total = parseFloat($(this).data("total"));

            
            const percentage = (saved / total) * 100;

            
            $(this).find(".progress-bar")
                .css("width", percentage + "%")
                .attr("aria-valuenow", percentage)
                .text(Math.round(percentage) + "%");
        });
    }

    updateGoalProgressBars();

    function calculateTotalProgress() {
        let totalSaved = 0;
        let totalRequired = 0;

        
        $(".goal-card").each(function () {
            const saved = parseFloat($(this).data("saved"));
            const total = parseFloat($(this).data("total"));

            totalSaved += saved;
            totalRequired += total;
        });

        const progressValue = totalSaved / totalRequired;

        $('#example').circleProgress({
            size: 230,
            value: progressValue,
            background: 'transparent',
            fill: {
                color: '#ffffff' 
            },
            thickness: 25
        });
    }

    calculateTotalProgress();

    
});