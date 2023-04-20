var pregnancy = document.querySelector("select[name=pregnancy]");
var surgeries = document.querySelector("select[name=last_surgeries]");
var submit = document.querySelector("form");

const status_check = () => {
  if (pregnancy.value === "3") {
    document.querySelector("select[name=pregnancy_result]").value = 5;
    document.querySelector("select[name=pregnancy_result]").disabled = true;
    document.querySelector("input[name=date_of_pregnancy]").value = "";
    document.querySelector("input[name=date_of_pregnancy]").disabled = true;
  } else if (pregnancy.value === "2") {
    document.querySelector("select[name=pregnancy_result]").value = 5;
    document.querySelector("select[name=pregnancy_result]").disabled = true;
    document.querySelector("input[name=date_of_pregnancy]").value = "";
    document.querySelector("input[name=date_of_pregnancy]").disabled = true;
  } else {
    document.querySelector("select[name=pregnancy_result]").disabled = false;
    document.querySelector("input[name=date_of_pregnancy]").disabled = false;
  }

  if (surgeries.value === "3") {
    document.querySelector("textarea[name=surgery_reasons]").value = "";
    document.querySelector("textarea[name=surgery_reasons]").disabled = true;
    document.querySelector("input[name=date_of_injury]").value = "";
    document.querySelector("input[name=date_of_injury]").disabled = true;
    document.querySelector("select[name=violent_death_causes]").value = 5;
    document.querySelector("select[name=violent_death_causes]").disabled = true;
    document.querySelector("textarea[name=place_where_injury_occurred]").value =
      "";
    document.querySelector(
      "textarea[name=place_where_injury_occurred]",
    ).disabled = true;
    document.querySelector("textarea[name=event_description]").value = "";
    document.querySelector("textarea[name=event_description]").disabled = true;
  } else if (surgeries.value === "2") {
    document.querySelector("textarea[name=surgery_reasons]").value = "";
    document.querySelector("textarea[name=surgery_reasons]").disabled = true;
    document.querySelector("input[name=date_of_injury]").value = "";
    document.querySelector("input[name=date_of_injury]").disabled = true;
    document.querySelector("select[name=violent_death_causes]").value = 5;
    document.querySelector("select[name=violent_death_causes]").disabled = true;
    document.querySelector("textarea[name=place_where_injury_occurred]").value =
      "";
    document.querySelector(
      "textarea[name=place_where_injury_occurred]",
    ).disabled = true;
    document.querySelector("textarea[name=event_description]").value = "";
    document.querySelector("textarea[name=event_description]").disabled = true;
  } else {
    document.querySelector("textarea[name=surgery_reasons]").disabled = false;
    document.querySelector("input[name=date_of_injury]").disabled = false;
    document.querySelector("select[name=violent_death_causes]").value = 1;
    document.querySelector(
      "select[name=violent_death_causes]",
    ).disabled = false;
    document.querySelector(
      "textarea[name=place_where_injury_occurred]",
    ).disabled = false;
    document.querySelector("textarea[name=event_description]").disabled = false;
  }
};

const to_sumit = () => {
  document.querySelector("select[name=pregnancy_result]").disabled = false;
  document.querySelector("input[name=date_of_pregnancy]").disabled = false;
  document.querySelector("textarea[name=surgery_reasons]").disabled = false;
  document.querySelector("input[name=date_of_injury]").disabled = false;
  document.querySelector("select[name=violent_death_causes]").disabled = false;
  document.querySelector(
    "textarea[name=place_where_injury_occurred]",
  ).disabled = false;
  document.querySelector("textarea[name=event_description]").disabled = false;
};

$(document).ready(status_check());

pregnancy.addEventListener("change", status_check);
surgeries.addEventListener("change", status_check);
submit.addEventListener("submit", to_sumit);
