const inputField = document.getElementById("fileInput");
const uploadField = document.querySelector(".upload__img-box");
const uploadBox = document.querySelector(".upload");
const closeBtn = document.querySelector(".exit__btn");
const upload_img_area = document.querySelector(".upload__img-icon");
const uploaded_img_prev_area = document.querySelector(".upload__box_one");
const upload_sol_prev_area = document.querySelector(".upload__box_two");

// Progress Bar Elements
const progress_bar_container = document.querySelector(".progress");
const user_uploaded_file_name = document.querySelector(".file-name");
const progress_per = document.querySelector(".percentage");
const progress_status_done = document.querySelector(".progress__status_done");
const progress_status_fail = document.querySelector(".progress__status_fail");
const progress_bar = document.querySelector(".progress__bar");
const file_size = document.querySelector(".file_size");

upload_img_area.addEventListener("click", function () {
  inputField.click();
});

inputField.addEventListener("change", function () {
  if (inputField.files.length == 0) return;

  progress_bar_container.classList.toggle("progress_bar_container--hide");
  const file = inputField.files[0];
  const formData = new FormData();

  formData.append("file", file);

  let fileName = file.name;
  if (fileName.length > 16) {
    fileName = `${fileName.slice(0, 12)}...`;
  }

  const xhr = new XMLHttpRequest();
  xhr.open("POST", "/upload", true);

  user_uploaded_file_name.textContent = `${fileName}`;
  xhr.upload.onprogress = function (event) {
    if (event.lengthComputable) {
      let percentage = (event.loaded / event.total) * 100;
      progress_bar.style.width = percentage + "%";
      progress_per.textContent = Math.floor(percentage) + "%";
      file_size.textContent = `${Math.floor(event.total / 1000)} KB`;
    }
  };

  xhr.onload = function () {
    if (xhr.status == 200) {
      const data = JSON.parse(xhr.responseText);
      show_uploaded_img(data);
      progress_per.classList.toggle("progress_per--hide");
      progress_status_done.classList.toggle("progress__status--hide");
    } else {
      const data = JSON.parse(xhr.responseText);
      show_uploaded_img(data);
    }
  };

  xhr.send(formData);
});

closeBtn.addEventListener("click", reset_app);

function show_uploaded_img(s) {
  if (s.status == 400) return;

  progress_bar_container.classList.toggle("progress_bar_container--hide");
  progress_bar.style.width = "0%";
  progress_per.textContent = "0%";
  file_size.textContent = "0 KB";
  uploadBox.classList.toggle("upload_dimension");
  upload_img_area.classList.toggle("hide_upload_area");
  uploaded_img_prev_area.classList.toggle("hide_upload_box");
  upload_sol_prev_area.classList.toggle("hide_upload_box");

  uploaded_img_prev_area.querySelector(
    "img"
  ).src = `static/uploads/${s.file_path}`;
  upload_sol_prev_area.querySelector(
    "img"
  ).src = `static/solution/sudoku_solution.png`;
}

function reset_app() {
  uploadBox.classList.toggle("upload_dimension");
  upload_img_area.classList.toggle("hide_upload_area");
  uploaded_img_prev_area.classList.toggle("hide_upload_box");
  upload_sol_prev_area.classList.toggle("hide_upload_box");

  uploaded_img_prev_area.querySelector("img").src = "";
  upload_sol_prev_area.querySelector("img").src = "";
}
