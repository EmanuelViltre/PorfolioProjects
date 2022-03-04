SELECT *
FROM PortfolioProject.. CovidDeaths
order by 3,4


--SELECT *
--FROM PortfolioProject.. CovidVaccionations
--order by 3,4

-- Select data that we I am going to use

Select Location, date, total_cases, new_cases, total_deaths, population
From PortfolioProject.. CovidDeaths
order by 1,2 

-- Looking at Total Cases vs Total Deaths

Select Location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 as DeathPercentage
From PortfolioProject.. CovidDeaths
where location like '%Argentina%'
order by 1,2 

--Looking at Total Cases vs Population
--Shows what porcentage of population got Covid

Select Location, date, population, total_cases, (total_cases/population)*100 as PercentPopulationInfected
From PortfolioProject.. CovidDeaths
where location like '%Argentina%'
order by 1,2 

-- Looking at countries with highest infection rate compared to population

Select Location, population, MAX(total_cases) as HighestInfectionCount, MAX((total_cases/population))*100 as PercentPopulationInfected
From PortfolioProject.. CovidDeaths
where continent is not null
--where location like '%Argentina%'
group by Location, population
order by PercentPopulationInfected desc

--Showing the countries with Highest Death Count per Population

Select Location, max(cast(Total_deaths as int)) as TotalDeathCount
From PortfolioProject.. CovidDeaths
where continent is not null
group by Location
order by TotalDeathCount desc


--Showing continents with the highest death count per population

Select continent, max(cast(Total_deaths as int)) as TotalDeathCount
From PortfolioProject.. CovidDeaths
where continent is not null
group by continent
order by TotalDeathCount desc

-- Global Numbers

Select date, sum(new_cases) as total_cases, SUM(cast(new_deaths as int)) as total_deaths, SUM(cast(New_deaths as int))/SUM(New_Cases)*100 as DeathPercentage
From PortfolioProject.. CovidDeaths
--where location like '%Argentina%'
where continent is not null
group by date
order by 1,2 

--Total cases across the world


Select  sum(new_cases) as total_cases, SUM(cast(new_deaths as int)) as total_deaths, SUM(cast(New_deaths as int))/SUM(New_Cases)*100 as DeathPercentage
From PortfolioProject.. CovidDeaths
--where location like '%Argentina%'
where continent is not null
--group by date
order by 1,2 


--Looking at Total Population vs Vaccinations
With PopvsVac (Continent, Location, Date, Population, New_Vaccinations, RollingPeopleVaccinated)
as
(
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(Cast(vac.new_vaccinations as bigint)) OVER (Partition by dea.location order by dea.location, dea.date) as RollingPeopleVaccinated
--, (RollingPeopleVaccinated/population)*100
from PortfolioProject..CovidDeaths dea
Join PortfolioProject..CovidVaccionations vac
	On dea. location = vac. location
	and dea.date = vac.date
where dea.continent is not null
--order by 2,3
)
Select *, (RollingPeopleVaccinated/population)*100
From PopvsVac


-- TEMP TABLE

DROP Table if exists #PercentPopulationVaccinated
Create Table #PercentPopulationVaccinated
(
Continent nvarchar(255),
Location nvarchar(255),
Date datetime,
Population numeric,
New_vaccinations numeric,
RollingPeopleVaccinated numeric,
)

insert into #PercentPopulationVaccinated
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(Cast(vac.new_vaccinations as bigint)) OVER (Partition by dea.location order by dea.location, dea.date) as RollingPeopleVaccinated
--, (RollingPeopleVaccinated/population)*100
from PortfolioProject..CovidDeaths dea
Join PortfolioProject..CovidVaccionations vac
	On dea. location = vac.location
	and dea.date = vac.date
--where dea.continent is not null
--order by 2,3

Select *, (RollingPeopleVaccinated/population)*100
From #PercentPopulationVaccinated

--Creating view to store data for later visulizations

Create View PorcentPopulationVaccinated as
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(Cast(vac.new_vaccinations as bigint)) OVER (Partition by dea.location order by dea.location, dea.date) as RollingPeopleVaccinated
--, (RollingPeopleVaccinated/population)*100
from PortfolioProject..CovidDeaths dea
Join PortfolioProject..CovidVaccionations vac
	On dea. location = vac.location
	and dea.date = vac.date
where dea.continent is not null
--order by 2,3

Select *
From #PercentPopulationVaccinated