<?php
session_start();
include("admin/db.php");
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if(isset($_POST['username'])) {
        try {
            $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

            $username = $_POST['username'];
            $query = "SELECT * FROM users WHERE username = '$username'";
            $result = $pdo->query($query);

            $user = $result->fetch(PDO::FETCH_ASSOC);

            /* Implement mailer logic to send password */
            if ($user) {
                $_SESSION['displayMessage'] = "Successfully sent password reset request!";
                header('Location: /forgot_password.php');
                exit;
            } else {
                $_SESSION['errorMessage'] = "Unable to process request, try again!";
                header('Location: /forgot_password.php');
                exit;
            }
        } catch (PDOException $e) {
            $_SESSION['errorMessage'] = 'Connection failed: ' . $e->getMessage();
            header('Location: /forgot_password.php');
            exit;
        }
    } else {
        header('Location: /login.php');
        exit;
    }
} else { ?>

<!DOCTYPE html>
<html lang="en">
<head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>MonitorsThree - Password Reset</title>
        <link rel="icon" type="image/x-icon" href="admin/assets/images/logo.ico">
        <!-- Global stylesheets -->
        <link href="https://fonts.googleapis.com/css?family=Roboto:400,300,100,500,700,900" rel="stylesheet" type="text/css">
        <link href="admin/assets/css/icons/icomoon/styles.css" rel="stylesheet" type="text/css">
        <link href="admin/assets/css/minified/bootstrap.min.css" rel="stylesheet" type="text/css">
        <link href="admin/assets/css/minified/core.min.css" rel="stylesheet" type="text/css">
        <link href="admin/assets/css/minified/components.min.css" rel="stylesheet" type="text/css">
        <link href="admin/assets/css/minified/colors.min.css" rel="stylesheet" type="text/css">
        <!-- /global stylesheets -->

        <!-- Core JS files -->
        <script type="text/javascript" src="admin/assets/js/plugins/loaders/pace.min.js"></script>
        <script type="text/javascript" src="admin/assets/js/core/libraries/jquery.min.js"></script>
        <script type="text/javascript" src="admin/assets/js/core/libraries/bootstrap.min.js"></script>
        <script type="text/javascript" src="admin/assets/js/plugins/loaders/blockui.min.js"></script>
        <!-- /core JS files -->

        <!-- Theme JS files -->
        <script type="text/javascript" src="admin/assets/js/core/app.js"></script>
        <!-- /theme JS files -->

</head>

<body>

        <!-- Page container -->
        <div class="page-container login-container">

                <!-- Page content -->
                <div class="page-content">

                        <!-- Main content -->
                        <div class="content-wrapper">

                                <!-- Content area -->
                                <div class="content">

                                        <!-- Password recovery -->
                                        <form action="#" method="POST">
                                                <div class="panel panel-body login-form">
                                                        <div class="text-center">
                                                            <div ><img src="admin/assets/images/logo.ico" style="width:100px;height:100px;"></img></div>
                                                                <h5 class="content-group">Password recovery <small class="display-block">We'll send you instructions in email</small></h5>
                                                        </div>

                                                        <div class="form-group has-feedback">
                                                                <input type="text" name="username" class="form-control" placeholder="Your username">
                                                                <div class="form-control-feedback">
                                                                        <i class="icon-user text-muted"></i>
                                                                </div>
                                                        </div>
                                    <?php
                               if (isset($_SESSION['errorMessage'])){
                                 echo "<div class='alert bg-danger alert-styled-left'>
                                                <button type='button' class='close' data-dismiss='alert'><span>×</span><span class='sr-only'>Close</span></button>
                                               " . $_SESSION['errorMessage'] . "
                                            </div>";
                                unset($_SESSION['errorMessage']);
                               } elseif (isset($_SESSION['displayMessage'])) {
                                 echo "<div class='alert bg-success alert-styled-left'>
                                                <button type='button' class='close' data-dismiss='alert'><span>×</span><span class='sr-only'>Close</span></button>
                                               " . $_SESSION['displayMessage'] . "
                                            </div>";
                                unset($_SESSION['displayMessage']);
                               }
                                ?>
                                                        <button type="submit" class="btn bg-blue btn-block">Reset password <i class="icon-arrow-right14 position-right"></i></button>
                                                </div>
                                        </form>
                                        <!-- /password recovery -->


                                        <!-- Footer -->
                                        <div class="footer text-muted">
                                                Copyright &copy; 2024. <a href="/">MonitorsThree</a>
                                        </div>
                                        <!-- /footer -->

                                </div>
                                <!-- /content area -->

                        </div>
                        <!-- /main content -->

                </div>
                <!-- /page content -->

        </div>
        <!-- /page container -->

</body>
</html>
<?php } ?>