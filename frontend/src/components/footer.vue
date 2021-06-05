<template>
  <div id="main">
    <body>
      <footer class="footer-32892 pb-0">
        <div class="site-section">
          <div class="container">
            <div class="row">
              <div class="col-md pr-md-5 mb-4 mb-md-0">
                <h3>About Us</h3>
                <p class="mb-4">
                  Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                  Laboriosam itaque unde facere repellendus, odio et iste
                  voluptatum aspernatur ratione mollitia tempora eligendi maxime
                  est, blanditiis accusamus. Incidunt, aut, quis!
                </p>
                <ul class="list-unstyled quick-info mb-4">
                  <li>
                    <a href="#" class="d-flex align-items-center"
                      ><span class="icon mr-3 icon-phone"></span> +1 291 3912
                      329</a
                    >
                  </li>
                  <li>
                    <a href="#" class="d-flex align-items-center"
                      ><span class="icon mr-3 icon-envelope"></span>
                      info@gmail.com</a
                    >
                  </li>
                </ul>

                <form action="#" class="subscribe">
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Enter your e-mail"
                  />
                  <input type="submit" class="btn btn-submit" value="Send" />
                </form>
              </div>
              <div class="col-md mb-4 mb-md-0">
                <h3>Latest Tweet</h3>
                <ul class="list-unstyled tweets">
                  <li class="d-flex">
                    <div class="mr-4">
                      <span class="icon icon-twitter"></span>
                    </div>
                    <div>
                      Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                      Facere unde omnis veniam porro excepturi.
                    </div>
                  </li>
                  <li class="d-flex">
                    <div class="mr-4">
                      <span class="icon icon-twitter"></span>
                    </div>
                    <div>
                      Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                      Facere unde omnis veniam porro excepturi.
                    </div>
                  </li>
                  <li class="d-flex">
                    <div class="mr-4">
                      <span class="icon icon-twitter"></span>
                    </div>
                    <div>
                      Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                      Facere unde omnis veniam porro excepturi.
                    </div>
                  </li>
                </ul>
              </div>

              <div class="col-md-3 mb-4 mb-md-0">
                <h3>Instagram</h3>
                <div class="row gallery">
                  <div class="col-6">
                    <a href="#"
                      ><img src="images/img_1.jpg" alt="Image" class="img-fluid"
                    /></a>
                    <a href="#"
                      ><img src="images/img_2.jpg" alt="Image" class="img-fluid"
                    /></a>
                  </div>
                  <div class="col-6">
                    <a href="#"
                      ><img src="images/img_3.jpg" alt="Image" class="img-fluid"
                    /></a>
                    <a href="#"
                      ><img src="images/img_4.jpg" alt="Image" class="img-fluid"
                    /></a>
                  </div>
                </div>
              </div>

              <div class="col-12">
                <div class="py-5 footer-menu-wrap d-md-flex align-items-center">
                  <ul class="list-unstyled footer-menu mr-auto">
                    <li><a href="#">Home</a></li>
                    <li><a href="#">About</a></li>
                    <li><a href="#">Our works</a></li>
                    <li><a href="#">Services</a></li>
                    <li><a href="#">Blog</a></li>
                    <li><a href="#">Contacts</a></li>
                  </ul>
                  <div class="site-logo-wrap ml-auto">
                    <a href="#" class="site-logo">
                      Colorlib
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </footer>
    </body>
  </div>
</template>

<script>
export default {}
</script>

<style scoped>
body{
    position: relative;
    padding-top:200px;
  }
h1,
h2,
h3,
h4,
h5,
h6,
.h1,
.h2,
.h3,
.h4,
.h5,
.h6 {
  font-family: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
    'Helvetica Neue', Arial, 'Noto Sans', sans-serif, 'Apple Color Emoji',
    'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
}

a {
  -webkit-transition: 0.3s all ease;
  -o-transition: 0.3s all ease;
  transition: 0.3s all ease;
}

a,
a:hover {
  text-decoration: none !important;
}

.content {
  height: 70vh;
}

.footer-32892 {
  background-color: #202126;
  padding: 7rem 0;
  color: #888;
  font-size: 16px;
}

.footer-32892,
.footer-32892 h3 {
  font-family: 'Poppins', sans-serif;
}

.footer-32892 h3 {
  font-size: 20px;
  color: #fff;
  margin-bottom: 30px;
}

.footer-32892 p {
  font-family: 'Source Serif Pro', serif;
}

.footer-32892 .row.gallery {
  margin-right: -5px;
  margin-left: -5px;
}

.footer-32892 .row.gallery > [class^='col-'],
.footer-32892 .row.gallery > [class*=' col-'] {
  padding-right: 5px;
  padding-left: 5px;
}

.footer-32892 .gallery a {
  display: block;
  margin-bottom: 10px;
  -webkit-transition: 0.3s all ease;
  -o-transition: 0.3s all ease;
  transition: 0.3s all ease;
}

.footer-32892 .gallery a:hover {
  opacity: 0.5;
}

.footer-32892 .quick-info li {
  color: #fff;
  font-size: 16px;
  margin-bottom: 10px;
}

.footer-32892 .quick-info li a {
  color: #fff;
}

.footer-32892 .quick-info li .icon {
  font-size: 20px;
  color: #f88020;
}

.footer-32892 .subscribe {
  position: relative;
}

.footer-32892 .subscribe .form-control {
  background-color: #292b31;
  -webkit-box-shadow: none;
  box-shadow: none;
  border-radius: 30px;
  height: 55px;
  padding-left: 30px;
  padding-right: 130px;
  border: none;
  color: #fff;
}

.footer-32892 .subscribe .form-control::-webkit-input-placeholder {
  color: #ccc;
  font-size: 14px;
}

.footer-32892 .subscribe .form-control::-moz-placeholder {
  color: #ccc;
  font-size: 14px;
}

.footer-32892 .subscribe .form-control:-ms-input-placeholder {
  color: #ccc;
  font-size: 14px;
}

.footer-32892 .subscribe .form-control:-moz-placeholder {
  color: #ccc;
  font-size: 14px;
}

.footer-32892 .subscribe .btn-submit {
  background: #f88020;
  height: 47px;
  border-radius: 30px;
  padding-left: 30px;
  padding-right: 30px;
  color: #fff;
  font-weight: bold;
  position: absolute;
  top: 4px;
  right: 4px;
  -webkit-box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.2);
  box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.2);
}

.footer-32892 .tweets li {
  margin-bottom: 20px;
  font-size: 15px;
  font-style: italic;
  font-family: 'Source Serif Pro', serif;
}

.footer-32892 .tweets li span {
  color: #fff;
}

.footer-32892 .footer-menu-wrap {
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  padding-top: 2rem !important;
  margin-top: 7rem;
}

.footer-32892 .footer-menu {
  margin-bottom: 0;
}

.footer-32892 .footer-menu li {
  display: inline-block;
}

@media (max-width: 767.98px) {
  .footer-32892 .footer-menu li {
    display: block;
  }
}

.footer-32892 .footer-menu li a {
  padding: 10px;
  display: inline-block;
  color: #fff;
}

@media (max-width: 767.98px) {
  .footer-32892 .footer-menu li a {
    display: block;
    padding-left: 0px;
  }
}

.footer-32892 .footer-menu li:first-child a {
  padding-left: 0;
}

.footer-32892 .site-logo {
  color: #fff;
  font-size: 20px;
}
</style>
