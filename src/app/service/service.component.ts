import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-service',
  standalone: true,
  imports: [HttpClientModule, FormsModule],
  templateUrl: './service.component.html',
  styles: ``
})
export class ServiceComponent {

  fileData: { title: string, value: string, lang: string, gender: string }[] = []
  voices: { title: string, value: string, lang: string, gender: string }[] = []
  languages: string[] = []

  languageFilter = ""
  genderFilter = ""

  constructor(route: ActivatedRoute, private http: HttpClient) {
    route.params.subscribe((params) => {
      this.getJSON(params['service']).subscribe((array) => {
        this.voices = array
        this.fileData = array
        this.languages = [...new Set(this.voices.map(voice => voice.lang))]
        this.genderFilter = ""
        this.languageFilter = ""
      })
    })
  }

  onChange() {
    this.voices = this.fileData
    this.voices = this.voices.filter((voice) => {
      return this.genderFilter == "" || this.genderFilter != "" && voice.gender == this.genderFilter
    })
    this.voices = this.voices.filter((voice) => {
      return this.languageFilter == "" || this.languageFilter != "" && voice.lang == this.languageFilter
    })
  }

  getJSON(service: string): Observable<any> {
    return this.http.get(`./assets/json/${service}.json`);
  }
}
