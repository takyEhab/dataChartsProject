const getAllData = async (expiryDate, formatedString) => {
  loading();
  const config = {
    method: "POST",
    body: JSON.stringify({
      expiryDate,
      formatedString,
    }),
  };
  const res = await fetch("/get-data", config);
  const data = await res.json();
  return data;
};

const getData = (data) => {
  return data.map((item) => ({
    time: new Date(`${item.Date}, ${item.Time}`).getTime() / 1000 + 330 * 60,
    open: item.Open * 1,
    high: item.High * 1,
    low: item.Low * 1,
    close: item.Close * 1,
  }));
};

const getDataoi = (data) => {
  return data.map((item) => ({
    time: new Date(`${item.Date}, ${item.Time}`).getTime() / 1000 + 330 * 60,
    value: item.Open_Interest * 1,
  }));
};

const displayChart = async (expiryDate, formattedString) => {
  const data = await getAllData(expiryDate, formattedString);
  showPage();
  document.getElementById("name").innerHTML = formattedString;
  const chartProperties = {
    width: 1120,
    height: 440,
    layout: {
      backgroundColor: "#131722",
      textColor: "#d1d4dc",
    },
    crosshair: {
      mode: LightweightCharts.CrosshairMode.Normal,
    },
    timeScale: {
      timeVisible: true,
      secondsVisible: true,
    },
    grid: {
      vertLines: {
        color: "#303030",
      },
      horzLines: {
        color: "#303030",
      },
    },
  };
  let domElement = document.getElementById("tvchart");
  domElement.innerHTML = "";
  const chart = LightweightCharts.createChart(domElement, chartProperties);
  const candleseries = chart.addCandlestickSeries();
  const klinedata = getData(data);
  candleseries.setData(klinedata);

  chart.timeScale().scrollToPosition(-20, false);
  var width = 27;
  var height = 27;

  var button = document.createElement("div");
  button.className = "go-to-realtime-button";
  button.style.top = chartProperties.height + 70 + "px";
  button.style.left = chartProperties.width - 75 + "px";
  button.style.color = "#4c525e";
  button.innerHTML =
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 14 14" width="14" height="14"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="2" d="M6.5 1.5l5 5.5-5 5.5M3 4l2.5 3L3 10"></path></svg>';
  document.body.appendChild(button);

  var timeScale = chart.timeScale();
  timeScale.subscribeVisibleTimeRangeChange(function () {
    var buttonVisible = timeScale.scrollPosition() < -5;
    button.style.display = buttonVisible ? "block" : "none";
  });

  button.addEventListener("click", function () {
    timeScale.scrollToRealTime();
  });

  button.addEventListener("mouseover", function () {
    button.style.background = "rgba(250, 250, 250, 1)";
    button.style.color = "#000";
  });

  button.addEventListener("mouseout", function () {
    button.style.background = "rgba(250, 250, 250, 0.6)";
    button.style.color = "#4c525e";
  });

  const dataOi = getDataoi(data);
  document.getElementById("OI").addEventListener("click", function () {
    activeOi(chart, dataOi);
  });
  // oi start
  // var volumeSeries = chart.addAreaSeries({
  //   topColor: "rgba(19, 68, 193, 0.2)",
  //   bottomColor: "rgba(0, 0, 0, 0.0)",
  //   lineColor: "rgba(255, 255, 255, 1)",
  //   lineWidth: 1.2,
  //   color: "#26a69a",
  //   priceFormat: {
  //     type: "open interest",
  //   },
  //   priceScaleId: "1",
  //   scaleMargins: {
  //     top: 0.85,
  //     bottom: 0,
  //   },
  // });

  // var klinedata2 = await getDataoi();

  // volumeSeries.setData(klinedata2);
  // oi end
};
function activeOi(chart, dataOi) {
  var volumeSeries = chart.addAreaSeries({
    topColor: "rgba(19, 68, 193, 0.2)",
    bottomColor: "rgba(0, 0, 0, 0.0)",
    lineColor: "rgba(255, 255, 255, 1)",
    lineWidth: 1.2,
    color: "#26a69a",
    priceFormat: {
      type: "open interest",
    },
    priceScaleId: "1",
    scaleMargins: {
      top: 0.85,
      bottom: 0,
    },
  });

  volumeSeries.setData(dataOi);
}

function showPage() {
  document.getElementById("loader").style.display = "none";
  document.getElementById("chart").style.display = "block";
  document.querySelector("#submitButton").disabled = false;
}
function loading() {
  document.getElementById("loader").style.display = "block";
  document.getElementById("chart").style.display = "none";
  document.querySelector("#submitButton").disabled = true;
}

let myForm = document.getElementById("myForm");
myForm.addEventListener("submit", function (e) {
  e.preventDefault();
  var data = new FormData(myForm);

  displayChart(
    data.get("date"),
    data.get("instrument") + data.get("strike") + data.get("CE_PE")
  );
});


function getStrikes() {
  document.getElementById("strike").innerHTML = "";
  $.ajax({
    type: "GET",
    url: `get-strikes/${$("#date option:selected").html()}`,
    success: function (response) {
      var select = document.getElementById("strike");
      for (var i = 0; i < response.length; i++) {
        var option = document.createElement("option");
        option.value = response[i];
        option.innerHTML = response[i];
        select.appendChild(option);
      }
    },
  });
}
getStrikes()
document.getElementById("date").addEventListener("change", getStrikes);
