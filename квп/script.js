function searchJobs() {
	const query = document.getElementById("search").value.toLowerCase();
	const jobsContainer = document.getElementById("jobs");
	jobsContainer.innerHTML = "";
	
	const jobs = [
		{ title: "Программист", company: "TechCorp" },
		{ title: "Дизайнер", company: "CreativeStudio" },
		{ title: "Маркетолог", company: "MarketPro" }
	];
	
	const filteredJobs = jobs.filter(job => job.title.toLowerCase().includes(query));
	
	if (filteredJobs.length > 0) {
		filteredJobs.forEach(job => {
			const jobElement = document.createElement("div");
			jobElement.innerHTML = `<h3>${job.title}</h3><p>${job.company}</p>`;
			jobElement.style.border = "1px solid #ddd";
			jobElement.style.padding = "10px";
			jobElement.style.margin = "10px 0";
			jobElement.style.background = "#fff";
			jobsContainer.appendChild(jobElement);
		});
	} else {
		jobsContainer.innerHTML = "<p>Вакансии не найдены</p>";
	}
}