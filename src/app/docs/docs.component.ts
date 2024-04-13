import { Component } from '@angular/core';
import { RouterLink, RouterModule, RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-docs',
  standalone: true,
  imports: [RouterOutlet, RouterLink, RouterModule],
  templateUrl: './docs.component.html',
  styles: ``
})
export class DocsComponent {
  items = [
    { title: 'Acapela', route: 'acapela' },
    { title: 'Cepstral', route: 'cepstral' },
    { title: 'IBM Watson', route: 'ibm-watson' },
    { title: 'Oddcast', route: 'oddcast' },
    { title: 'StreamElements', route: 'stream-elements' },
    { title: 'Streamlabs', route: 'stream-labs' },
    { title: 'VoiceForge', route: 'voice-forge' },
  ]
}
