import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Company} from "./models";
import {Vacancy} from "./models";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class CompanyService {
  BASE_URL  ='http://127.0.0.1:8000/'
  constructor(private client : HttpClient) { }
  getCompany() : Observable<Company[]> {
    return this.client.get<Company[]>(`${(this.BASE_URL)}/api/companies`)
  }
}
