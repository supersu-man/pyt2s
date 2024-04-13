import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [RouterLink],
  templateUrl: './home.component.html',
  styles: ``
})
export class HomeComponent {

  copied = false

  copy() {
    navigator.clipboard.writeText("pip install pyt2s")
    this.copied = true
  }
}
