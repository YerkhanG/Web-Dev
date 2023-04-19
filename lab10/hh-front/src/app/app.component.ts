import { Component, OnInit } from '@angular/core';
import { Company } from './models';
import { Vacancy} from "./models";
import {CompanyService} from "./company.service";
import {VacancyService} from "./vacancy.service";
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'hh-front';
  companies: Company[] = [];
  vacancies : Vacancy[] = [];
  Show(company : Company){
      this.comp = company.name;
  }
  comp = "";
  constructor(private companyService : CompanyService, private vacancyService : VacancyService) {
  }
  ngOnInit() {
    this.companyService.getCompany().subscribe((data1)=> {
      this.companies = data1;
    })
  }
  getVacancies(company_id: number){
    this.vacancyService.getVacancy(company_id).subscribe((data:Vacancy[])=>{
      console.log(data);
      this.vacancies = data;
    })
  }
}
