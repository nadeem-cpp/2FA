// <!-- jquery -->
// <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script>
// <!--jquery data table cdn -->
// <link rel="stylesheet" href="https://cdn.datatables.net/1.13.5/css/jquery.dataTables.css" />
// <script src="https://cdn.datatables.net/1.13.5/js/jquery.dataTables.js"></script>

$(document).ready(function () {
    let timerSeconds = 60;
    let timerInterval;

    // Function to update the timer text
    function updateTimer() {
        $('#timer').text(timerSeconds);
        if (timerSeconds <= 0) {
            clearInterval(timerInterval);
            $('#timerText').hide();
            $('#resendOtpBtn').show();
        }
        timerSeconds--;
    }

    // Function to generate individual OTP input fields
    function generateOtpFields(otpLength) {
        let otpInputGroup = $('#otpInputGroup');
        otpInputGroup.empty();  // Clear existing fields
        for (let i = 0; i < otpLength; i++) {
            otpInputGroup.append('<input type="text" maxlength="1">');
        }
    }

    // Start the timer when the page loads
    timerInterval = setInterval(updateTimer, 1000);

    // Resend OTP button click event
    $('#resendOtpBtn').on('click', function () {
        // Simulate sending OTP to API (replace with your actual AJAX call)
        alert('Resending OTP...');
        // Reset timer and show it again
        timerSeconds = 60;
        $('#timerText').show();
        $('#resendOtpBtn').hide();
        timerInterval = setInterval(updateTimer, 1000);
        // Generate new OTP input fields
        generateOtpFields(6);  // Change the OTP length as needed
    });

    // Form submit event
    $('#otpForm').on('submit', function (e) {
        e.preventDefault();
        // Collect OTP from input fields
        let enteredOtp = '';
        $('.otp-digit').each(function () {
            enteredOtp += $(this).val();
        });
        // Simulate sending OTP to API (replace with your actual AJAX call)
        $.ajax(
            {
                url: '/user/auth',  // Update with your actual URL
                type: 'POST',
                contentType: "application/json",
                data: JSON.stringify({
                    otp: enteredOtp,
                }),
                success: function (response) {
                    $("#response").val(response)
                    console.log(response);
                    },
                error: function (error) {
                    $("#response").text(error.statusText)
                    console.error(error);
                }
            }
            );
    }
    );

    // Initial generation of OTP input fields
    generateOtpFields(6);  // Change the OTP length as needed
});