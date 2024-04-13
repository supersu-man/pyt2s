import { Routes } from '@angular/router';
import { ServiceComponent } from './service/service.component';
import { HomeComponent } from './home/home.component';
import { DocsComponent } from './docs/docs.component';

export const routes: Routes = [
    { path: '', component: HomeComponent },
    { path: 'docs', component: DocsComponent, children: [
        { path: ':service', component: ServiceComponent },
        { path: '**', redirectTo: 'acapela' }
    ]},
    { path: '**', redirectTo: '' }
];
